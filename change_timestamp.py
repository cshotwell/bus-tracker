from app import db, models
import datetime
from sys import argv

def change_timestamp(tweet_id):
    tweet = models.Tweet.query.filter_by(id=tweet_id).first()
    tweet.timestamp = datetime.datetime(2014, 2, 1, 18, 00, 20, 179434)
    db.session.add(tweet)
    db.session.commit()

if __name__ == '__main__':
    tweet_id = int(argv[1])
    change_timestamp(tweet_id)
