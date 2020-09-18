# http://docs.tweepy.org/en/latest/getting_started.html#hello-tweepy
import tweepy
from os import environ
import time

consumer_key = environ.get('TWITTER_API_KEY')
consumer_secret = environ.get('TWITTER_API_SECRET_KEY')
access_token = environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#! Get my user information
# user = api.me()
# print(user)

#! Get recent tweets from timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

#! Follower Bot
#+ Pagination (Cursor) - http://docs.tweepy.org/en/latest/cursor_tutorial.html?highlight=cursor
#- We use pagination a lot in Twitter API development. Iterating through timelines, user lists, direct messages, etc. 
#+ RateLimitError - http://docs.tweepy.org/en/latest/api.html?highlight=ratelimit#RateLimitError
#- Is raised when an API method fails due to hitting Twitter’s rate limit. Makes for easy handling of the rate limit specifically.
def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except StopIteration:
        print("") 
    except tweepy.RateLimitError:
        #! Stops the code for 1 sec
        time.sleep(1000)

for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name == 'username':
        follower.follow()

#! Search
#+ http://docs.tweepy.org/en/latest/api.html?highlight=search#search-methods
#- Returns a collection of relevant Tweets matching a specified query.

search_string = 'javascript'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as error:
        print(error.reason)
    except StopIteration:
        break
