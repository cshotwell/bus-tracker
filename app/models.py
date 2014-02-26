from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    photo_url = db.Column(db.String(120), unique = True)
    bus = db.Column(db.String(50))
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    tweets = db.relationship('Tweet', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

