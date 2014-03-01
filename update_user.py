from app import db
from app import models
import fetch_tweets
import datetime
from sqlalchemy import asc
from sqlalchemy.sql.expression import nullsfirst as nullsfirst


def update_least_updated():
    users = models.User.query.order_by(asc(models.User.last_updated).nullsfirst()).all()
    print users
    user = users[0]
    user.last_updated = datetime.datetime.utcnow()
    db.session.add(user)
    db.session.commit()
    print user

    fetch_tweets.fetch_tweets(user.username, user.bus)

if __name__ == '__main__':
    update_least_updated()
