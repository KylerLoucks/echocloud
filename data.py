import os
API_KEY = os.environ['AV_API_KEY']


TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']



try:
    TICKER = os.environ['BLOCKCHAIN_SYMBOL']
except:
    TICKER = "BTC"
    print("Couldn't find 'BLOCKCHAIN_SYMBOL' environment variable. Using default: BTC")
    pass