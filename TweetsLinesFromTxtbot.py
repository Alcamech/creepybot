#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original script (kept up to date): https://github.com/robincamille/bot-tutorial/blob/master/mybot2.py

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.


# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet

filename = open('TheRaven.txt','r')
tweettext = filename.readlines()
filename.close()

for line in tweettext[0:108]: #Lines 0-108
        api.update_status(line)
        print(line)
        time.sleep(15) # Sleep for 15 seconds

print("All done!")

# To quit early: CTRL+C and wait a few seconds
