#Import tweepy and tweepy credentials
import tweepy
from low_ticket_cred import consumer_key, consumer_secret, access_token, access_token_secret, twilio_account_sid, twilio_auth_token

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

from twilio.rest import TwilioRestClient

client = TwilioRestClient(twilio_account_sid, twilio_auth_token)


import time
import datetime
'''
public_tweets = api.home_timeline(count = 10) #figure out how to return more than 20 results
for tweet in public_tweets:
    #if "bicycle" in tweet.text.lower():
	print "{0} said: \"{1}\"".format(tweet.user.screen_name, tweet.text)
'''
#You could also build this list using raw_input

venue_handles = ["blackcatdc", "uhalldc", "930club", "dc9nightclub", "rocknrollhotel"]


for handle in venue_handles:
	time.sleep(1) 
	venue_tweets = api.user_timeline(handle)
	for tweet in venue_tweets:
		if "low ticket warning" in tweet.text.lower() or "low ticket alert" in tweet.text.lower():
			message = client.messages.create(body="{0} just tweeted: {1}".format(tweet.user.screen_name, tweet.text),
			to="+18475420232",
			from_="+12242315634")
		else:
			print "No warnings from {0} at {1}".format(tweet.user.screen_name, datetime.datetime.now())
	
#Stuff I'd like to add/figure out:
## Can we create a list of bands we care about and it'll only alert us about those shows?
### Possibly pull it from a Google Spreadsheet? Or a Spotify playlist or Bandcamp if we want to get rull complicated with APIs?
## What language do venues use in "low ticket" tweets and do they consistently use the same language? (Black Cat always says "LOW TICKET ALERT")
### Ooh, that could be a good way to determine which venue sent the tweet, if they all use different language and use it consistently (but it's actually probably easier/more reliable to just store the tweeter's handle in the dictionary with the tweet)
