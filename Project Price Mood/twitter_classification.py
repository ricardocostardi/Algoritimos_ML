import tweepy
from textblob import TextBlob

consumer_key = 'Ib0e4W0zBZyN6p3TRGGQc0Lf8'
consumer_secret = 'vlHL2FN0UkAJgG91PsxiZQJfzo7EqWxqFYYOP98Ev8B3ajnew'
access_token = '2486454853-R95bIDHlXWuhRwBmAT7inwzWV86wmMSM1LC4Ri'
access_token_secret = 'Lf6Xj3nQCwYtH9rvBhvjUVfqyGGWqdrLnLR0PwUntQSP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('snl')

for tweet in public_tweets[0:100]:
	#print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
