'''
Jake Sylvestre 
Attempts to Guess Age
'''

import TwitterUtility
import sqlite3
from nltk.corpus import stopwords

def find_age(name):
	tweets = TwitterUtility.get_tweets(name)

	words = freq_finder(tweets)

	conn = sqlite3.connect('database.db')
	c = conn.cursor()
 
	#for word in words:

def freq_finder(tweets):
	words = dict()
	
	stop = stopwords.words('english')

	for tweet in tweets:

		twits = tweet.split(' ')
		
		for twit in twits:
			if twit in stop:
				continue

			if twit in words:
				tel = words[twit]
				del words[twit]
				words[twit] = tel + 1 

			else:
				words[twit] = 1
			return words


