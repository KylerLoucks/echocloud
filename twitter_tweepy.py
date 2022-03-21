import tweepy
from data import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET

# pip install tweepy

# Authenticate:
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def send_tweet(message: str, media_location: str=None):
    media = api.media_upload(filename=media_location)
    tweet = api.update_status(status=message, media_ids=[media.media_id_string]) # send tweet
    print("TWEETED: ")

