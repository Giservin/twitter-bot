import os
import tweepy
import time

api_key = os.environ['API_KEY']
api_key_secret = os.environ['API_KEY_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

try:
	api = tweepy.API(authenticator, wait_on_rate_limit=True)
except FailToConnect:
	print('Failed to connect')

while True:
	file = open('count.txt', 'r')
	day = int(file.read())
	try:
		api.update_status('Day '+ str(day)+ ' : No')
	except FailToConnect:
		print('Failed to connect')
	file = open('count.txt', 'w')
	day = day+1
	file.write(str(day))
	time.sleep(24*3600)

