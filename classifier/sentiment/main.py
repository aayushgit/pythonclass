import tweepy
from textblob import TextBlob

CONSUMER_KEY = 'tmqkengI7kRvu8mCqz2Aup4Y7'
CONSUMER_SECRET = 'mpWObDLMK9Sx64bYUmXj7c7wVTzyg1xlUAoq1vlK8EAgfHokXP'
ACCESS_TOKEN = '593201197-dsIDuMxEH02bpJLL2WnRFmf9SrMo8FNhuaXVdcxi'
ACCESS_TOKEN_SECRET = '7ZuJhrAaFOKrT0mPy59659tPbUO1pAC5VxrzlHS2NRjF1'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
public_tweets = api.search('Tesla')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

