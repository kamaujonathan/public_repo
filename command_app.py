import json
import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


ACCESS_TOKEN = '37397537-An3haUzZJvsxX3uc3sSainvLuExZxpFvwokSTD7am'
ACCESS_SECRET = 'i6MC45o3rQVxcDIwu21tOoL1dZMbHJWzWNGDjaCZlSSRP'
CONSUMER_KEY = 'gTJmH2GCpKOjmV9DSaC7Bhwbn'
CONSUMER_SECRET = 'IirJvS6zmv4gZt522vkukc8pWC3X21CvJqFVVtIhbXq2yqfmxC'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


twitter_line = TwitterStream(auth=oauth)


iterate = twitter_line.statuses.sample()


tweets = 1000
for tweet in iterate:
    tweets -= 1
    print json.dumps(tweet)  
    
   
       
    if tweets <= 0:
        break 
