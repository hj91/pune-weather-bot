# -*- coding: utf-8
#!/usr/bin/env python

# posts pune weather to Twitter. 
#(c) Harshad Joshi, 2012.
# email - firewalrus at gmail dot com
# replace pune with your native place. 

# you can find this bot in action on twitter - @puneripunekar

import sys,feedparser,pywapi,time
import datetime
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


api = tweepy.API(auth)

google_result = pywapi.get_weather_from_google('Pune')

#print google_result

#print google_result["current_conditions"]


e=datetime.datetime.now()
f=str(e)

b = f+" "+'Current temperature of #Pune is'+">> "+google_result['current_conditions']['temp_c']+" degrees C\n" + ","+google_result['current_conditions']['humidity'] 

#+", "

#+ google_result['current_conditions']['wind_condition']+" #pune"

c=google_result['current_conditions']['temp_c']+' degrees C'+u' लेकोहो...किती ही उष्णता .!! आमच्या वेळी हे नव्हतं !'
d=u' पर्यावरणाचा ऱ्हास म्हणजे गळ्याला फास..! #pune'

api.update_status(c+d)
api.update_status(b)

print 'posted to twitter'
