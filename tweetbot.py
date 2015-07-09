import tweepy
import config
import cPickle as pickle
from markov import *

if __name__=="__main__":
	train_bool = False
	filename = "KamaSutra.txt"
	dicname = "dic_pre2.txt"
	if train_bool:
		f = open(filename, 'r')
		dic = mapText(f.read(), prefix=2, dic={})
		with open(dicname, 'wb') as myFile:
			pickle.dump(dic, myFile)
	with open(dicname, 'rb') as myFile:
		dic = pickle.load(myFile)
	# print message, len(message)

	auth = tweepy.OAuthHandler(config.consumer_token, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	api = tweepy.API(auth)

	while True:
		message = getChain(dic)
		print message
		response = raw_input("tweet? ").lower()
		if response and response[0] == "y":
			tweet = api.update_status(status=message)
			name = str(tweet.author.screen_name)
			tweet_id = str(tweet.id)
			permalink = "https://twitter.com/" + name + "/status/" + tweet_id
			print permalink + "\n"