'''
Jake Sylvestre
Automating Learning Script API
'''  

import TwitterUtility
import lexstore
import sqlite3
import random

def choose():
	lexstore.create_db()
	empty = []
	ages = ['teen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'other']#TODO switch to global vars for this
	hashtags = [['freshmen', 'sophmore', 'junior', 'senior', 'turned1'],['turned2', '21bitch'],['turned3', '30thbirthday'],['turned4'], ['turned5']]
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	c.execute('''SELECT * FROM db''')
	rows = c.fetchall()
	#if (rows == empty):#Let's keep words/word frequency even
	if True:#testing
		dimension1 = random.randrange(len(hashtags))
		dimension2 = random.randrange(len(hashtags[dimension1]))
		search(ages, hashtags, dimension1, dimension2)
	for age in ages:
		c.execute(''' SELECT * FROM db WHERE 'group' = ?;''', (age,))#Get groups so we can count words
		groups = c.fetchall()
	#for group in groups:
	#		print(groups)

def search(ages, hashtags, cord1, cord2):
	names = []
	hashtag = hashtags[cord1][cord2]
	if hashtag[0:6] == "turned":
		for num in range(8):
			num += 1
			hashtag = hashtag + str(num)
			names.append(TwitterUtility.get_hashtag_names(hashtag))
	else:
		names.append(TwitterUtility.get_hashtag_names(hashtag))
	for namely in names:
		for name in namely:
			res = lexstore.insert_user(name, ages[cord1])
			if res == False:
				tweets = TwitterUtility.get_tweets(name)
				#print("OK")
				#print(tweets)
				for tweet in tweets:
					print(tweet)
					lexstore.insert(tweet, ages[cord1])
choose()