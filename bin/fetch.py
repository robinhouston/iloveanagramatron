#!/usr/bin/python
# -*- encoding: utf-8 -*-
from __future__ import division

import datetime
import json
import re
import sys

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

def is_anagram(a, b):
    return sorted(re.sub(r"[^a-z]", "", a.lower())) == sorted(re.sub(r"[^a-z]", "", b.lower()))

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
tweet_pairs = []
prev_tweet = None
for status in tweepy.Cursor(api.user_timeline, screen_name="anagramatron").items():
    if not hasattr(status, "retweeted_status"):
        continue
    
    s = status.retweeted_status
    this_tweet = (s.id_str, s.text)
    if prev_tweet is not None and is_anagram(this_tweet[1], prev_tweet[1]):
        tweet_pairs.append((prev_tweet, this_tweet))
    prev_tweet = this_tweet

    if len(tweet_pairs) == N: break

for (a, b) in tweet_pairs:
    print (u"\t// %s → %s\n\t\t[\"%s\", \"%s\"]," % (a[1], b[1], a[0], b[0])).encode("utf-8")
