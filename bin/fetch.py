#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division

import datetime
import json

import tweepy
import tweepy.binder

CONSUMER_KEY = "Xe82j6WmKD9d6lGhVHMrT2gwT"
CONSUMER_SECRET = "jvBf480lIPUtPHju9zORgtZ5cBdZpk6ssaqhqeHFdxXhgpELED"
ACCESS_TOKEN = "34650516-OfZ8Eo7mqjodBCNIylqSMbcOabrXRKnl6WZ2q84Pb"
ACCESS_TOKEN_SECRET = "NgrNU3RScUAu2kOEQ5dHgzpselVFZcDLM8xWD0HH4iRNM"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

epoch = datetime.datetime.utcfromtimestamp(0)

for status in tweepy.Cursor(api.user_timeline, screen_name="anagramatron").items():
    if not hasattr(status, "retweeted_status"):
        continue
    
    s = status.retweeted_status
    url = "https://twitter.com/{screen_name}/status/{id}".format(screen_name=s.user.screen_name, id=s.id_str)
    print api.get_oembed(url=url)
    break
    
    print json.dumps({
        "url": url,
        "screen_name": s.user.screen_name,
        "name": s.user.name,
        "text": s.text,
        "created_at": (s.created_at - epoch).total_seconds(),
    })
    print

