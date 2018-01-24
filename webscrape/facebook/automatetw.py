import twitter

CONSUMER_KEY = 'tmqkengI7kRvu8mCqz2Aup4Y7'
CONSUMER_SECRET = 'mpWObDLMK9Sx64bYUmXj7c7wVTzyg1xlUAoq1vlK8EAgfHokXP'
ACCESS_TOKEN = '593201197-dsIDuMxEH02bpJLL2WnRFmf9SrMo8FNhuaXVdcxi'
ACCESS_TOKEN_SECRET = '7ZuJhrAaFOKrT0mPy59659tPbUO1pAC5VxrzlHS2NRjF1'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

users = api.GetFriends()

print([u.screen_name for u in users])