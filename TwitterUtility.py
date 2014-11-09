'''
Jake Sylvestre
Twitter Utility
Gets Tweets off Twitter using a skiddie-import strips them of all unnecesary information
'''

from TwitterAPI import TwitterAPI

def get_tweets(user):
	f = open('keys.txt', 'r')
	lines = f.readlines()
	tweets = []
	api = TwitterAPI(consumer_key=lines[0],
	                  consumer_secret=lines[1],
	                  access_token_key=lines[2],
	                  access_token_secret=lines[3])  
	                  #TODO A PRIORI PUSH PUT THESE VALUES IN A txt FILE OR EVEN BETTER MAKE A CLI TO GET THESE FROM THE USER  
	r = api.request('statuses/home_timeline', {'count':200})
	for item in r.get_iterator():
		try:
			tweets.append(item['text'])
		except:
			continue
	return tweets

def get_hashtag_names(hashtag):
	f = open('keys.txt', 'r')
	lines = f.readlines()
	tweets = []
	api = TwitterAPI(consumer_key=lines[0],
	                  consumer_secret=lines[1],
	                  access_token_key=lines[2],
	                  access_token_secret=lines[3])  
	tosearch = '#' + hashtag
	r = api.request('search/tweets', {'q':tosearch})
	for tweet in r:
		names.append(tweet['user']['screen_name'])
	return names
