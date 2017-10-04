import tweepy
import sys
import random

##########
# IMPORTANT!
#
# Enter your twitter handle on the next line for grading purposes:
#
# Twitter Handle: RyanZlupton

# ---- Add Twitter API Credentials--
CONSUMER_KEY = 'ky1VGf9Vshydz7O9m1huGr5cE'
CONSUMER_SECRET = 'L5jO7WNpHrSmWEzhUBdTkaQa9mTQcfTmeTWHg721Bgq2sPknXL'
ACCESS_TOKEN = '913468001776697344-OpyLL7GxrErejUtE4n2QdcloQnS9L2b'
ACCESS_TOKEN_SECRET = 'eiGmT8izWXl8phakvov5oGapFuTU3sWDfRB46z7sZ3VWl'
# ----------------------------------

# This function logs your bot in to Twitter.
# You should not need to modify this code.
def getTwitterApiHandle():
    # Twitter authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

# Demonstration function
def helloWorld(api):
        api.update_status('Hello world.')

# Problem 1
def randomTweetGenerator(api):
    list1 = open('file1.txt').read().splitlines()
    list2 = open('file2.txt').read().splitlines()
    list3 = open('file3.txt').read().splitlines()
    for i in range(1,12):
        rand1 = random.choice(list1)
        rand2 = random.choice(list2)
        rand3 = random.choice(list3)

        tweet = rand1 + ' is ' + rand2 + ' ' + rand3
        api.update_status(tweet)

# Problem 2
def secretMessage(api, username):
    # <your code goes here >
    tweet = 'HELPIMTRAPPEDINATWITTERBOTFACTORY'
    tweets = api.user_timeline('FMSBotFriend')
    for tweet1 in tweets:
        json = tweet1._json
        tweetText = json['text']
        for C in tweetText:
            if C.isupper():
                print(C)

# Are the 20 tweets stored in a list or just "tweets"
# Extract capitalized letters in reverse chronological order
# Problem 3
def custom(api):
    # <your code goes here>
    clever = 'Do something clever'
    searchtext = 'food stamps'
    clever1 = api.search(q=searchtext)
    for result in clever1:
        sn = result.user.screen_name
        message = "Would you buy $5 fully prepared, fresh, healthy dinners? Would you buy in advance and pick it up from a local school? Why?!"
        api.send_direct_message(sn, text=message)

# Select mode based on command-line argument
# You should not need to modify this code
if __name__ == "__main__":
    api = getTwitterApiHandle()

    if len(sys.argv) < 2:
        print ('Not enough arguments')
        sys.exit()

    mode = sys.argv[1]
    if mode == 'hello':
        helloWorld(api)
    elif mode == 'random':
        randomTweetGenerator(api)
    elif mode == 'secret':
        if len(sys.argv) != 3:
            print ('No username specified.')
        else:
            secretMessage(api, sys.argv[2])
    elif mode == 'custom':
        custom(api)
    else:
        print('Error: unrecognized mode')
