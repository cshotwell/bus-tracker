import os
import sys
import base64
import httplib
import json
import time
import datetime
from lib import twitter_api

from app import db, models
from config import SQLALCHEMY_DATABASE_URI
from config import basedir
from config import CONSUMER_KEY
from config import CONSUMER_SECRET

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET

def fetch_tweets(username, bus):
    username = username.lower()
    api = twitter_api.Api(consumer_key, consumer_secret)
    results = api.get_timeline(username)
    for tweet in results: #iterate tweet results
        tweet_user = tweet['user']
        if tweet_user['screen_name'].lower() != username: #if user does not match, skip it.
            continue
        user = models.User.query.filter_by(username=username).first()
        if not user: #if there is no user, save this one
            user = models.User(username=username, photo_url=tweet_user['profile_image_url'], bus=bus, role=models.ROLE_USER)
            db.session.add(user)
            db.session.commit()
        tweet_id = tweet['id']
        tweet_already_here = models.Tweet.query.filter_by(tweet_id=str(tweet_id)).first()
        if tweet_already_here:
            continue
        coordinates = tweet['coordinates']
        if not coordinates: #skip this if there aren't any coordinates
            continue
        unpacked_coordinates = coordinates['coordinates']
        lat, lon = unpacked_coordinates
        time_struct = time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
        time_struct = datetime.datetime(*time_struct[0:6])
        twit = models.Tweet(tweet_id=str(tweet_id), body=tweet['text'], timestamp=time_struct, lat=lat, lon=lon, author=user)
        db.session.add(twit)
        db.session.commit()

def main():
    username = 'kristine_hines'
    bus = 'Midwest'
    fetch_tweets(username, bus)

if __name__ == '__main__':
    main()
