#Author: Wsgsec 

import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#print out user info
user = api.me()
print (user.name)  
print (user.screen_name)
print (user.followers_count)

search = "#infosec"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(400)

# Follow people back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.followers_count <= 100: #only follow back people with over 100 followers 
    print(follower.name)
    follower.follow()


# like my own tweets & retweet certain tweets based on the keyword defined in 'search' var 
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):   
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
