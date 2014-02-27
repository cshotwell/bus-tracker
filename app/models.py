from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    photo_url = db.Column(db.String(120))
    bus = db.Column(db.String(50))
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    tweets = db.relationship('Tweet', backref = 'author', lazy = 'dynamic')

    @property
    def serialize(self):
        return {
            'id'        : self.id,
            'username'  : self.username,
            'photo_url' : self.photo_url,
            'bus'       : self.bus,
            'tweets'    : self.serialize_tweets
        }

    @property
    def serialize_tweets(self):
        return [tweet.serialize for tweet in self.tweets]


    def __repr__(self):
        return '<User %r>' % (self.username)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tweet_id = db.Column(db.String(50), unique = True)
    body = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lat = db.Column(db.String(50))
    lon = db.Column(db.String(50))

    @property
    def serialize(self):
        return {
            'id'        : self.id,
            'body'  : self.body,
            'timestamp' : dump_datetime(self.timestamp),
            'lat'    : self.lat,
            'lon'    : self.lon
        }

    def __repr__(self):
        return '<Post %r>' % (self.body)

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

