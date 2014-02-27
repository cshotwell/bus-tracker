#Likely need to rip all of this out. only should serve as reference
import os
import sys
import base64
import httplib
import json
import time
import datetime

BASE_DIR = os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.append(BASE_DIR)

import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

os.environ['PYTHONPATH'] = BASE_DIR
os.environ['DJANGO_SETTINGS_MODULE'] = 'ingenuity_festival.settings'

import urllib
from django.conf import settings

from ingenuity_festival.app.tweets.api import Api 
from ingenuity_festival.app.tweets.models import User, Status, Media

from ingenuity_festival import settings

consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET

def run():
    api = Api(consumer_key, consumer_secret)
    results = api.get_search('ingenuityfest')
    from django.utils.encoding import smart_str

    for tweet in results['statuses']:
        tweet_user = tweet['user']

        user = User(user_id=smart_str(tweet_user['id_str']), user_name=smart_str(tweet_user['screen_name']), profile_image=smart_str(tweet_user['profile_image_url']))
        user.save()

        time_struct = time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
        time_struct = datetime.datetime(*time_struct[0:6])
        status = Status(status=smart_str(tweet['text']), time_post=time_struct, user=user)
        status.save()
