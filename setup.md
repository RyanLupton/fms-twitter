In assignment 5 you will create a Twitter bot which will send and receive tweets on the Twitter platform on your behalf. This document provides some background and walks through the necessary setup tasks.


# Background: APIs

APIs, or “Application Programming Interfaces,” are the hidden backbone of our modern world. They allow programs to collaborate with one another -- even when the programs are on different computers. On the web, you can think of APIs like a telephone system: when one application wants to get information from or give instructions to another, it "calls" the second application’s API.

For example, if you wanted to build an app that showed users the nearest restaurants that their friends liked, you could use the Yelp API (to get restaurant data) and the Facebook API (to get data about what the user’s friends’ like). When a user opened your app, the application’s code would “call” the Yelp and Facebook APIs to get the data that it needed.

APIs do all of this by exposing a piece of the software’s internal data and functionality to the outside world in a controlled way. That allows for one application to share data and perform actions on one another’s behalf without requiring software developers to share all of their code. We have worked with the Spotify API in class. For this assignment, you will work with the Twitter API.

Read more about APIs here: [APIs: How the Internet Works Behind the Scenes](https://medium.com/@michaelrbock/apis-how-the-internet-works-behind-the-scenes-690288634c32)

## API keys

"API keys" are used as a way to authenticate developers who want access to an API. They enable an application to identify itself to the API, and sometimes to prove that a user has granted the application permission to interact with her account.

Often, anyone can get an API key with basic privileges. For example, anyone with a Twitter account can sign up to get a key to use Twitter's public API. After signing in with your Twitter account you can request an API key, which will then be tied to your Twitter account. This key will give you access to basic Twitter functionality like search, and will also give you access to functionality specific to your account, like direct messages and retweeting.


## Setup

We will be using the [tweepy](http://www.tweepy.org) library, which will make it easier to interact with the Twitter API.

**Step 1: Create Twitter Account**

First, you need to create a twitter handle to tweet from. DO NOT use an existing Twitter account. First, your bot will be tweeting out various inane messages you might not want coming from your regular Twitter account. Second, when you interact with the Twitter API, you can modify the data in the associated account. If your program has bugs, you might send out gibberish tweets or delete your old tweets. Don't take those risk.

A few notes:

* We recommend that you put "FMS" somewhere in the username of your new account.
* Pay attention to which account you are logged into Twitter as! Don't accidentally send FMS tweets from your regular account, or send regular tweets from your FMS account.
* If you already have a Twitter account, you will need to use a different email address when signing up for this one. You could use your Cornell address (if not already in use for a Twitter account), or you could sign up for a new Gmail/Outlook.com/Yahoo/etc. email account.
* You will need to add your mobile phone number to the account.


**Step 2: Get API Credentials**

Next, you need to get the API keys for the new account so that Twitter knows it's really you trying to read and send messages when you connect using your bot rather than the Twitter website or app.


1. Navigate to https://apps.twitter.com/ and click the button to create a new app (you can use https://tech.cornell.edu/ as the 'website')
2. Navigate to the "Keys and Access Tokens" tab
3. Click the "Create my access token" button
4. Copy your credentials to the `twitterbot.py` file. There are four items you will need to copy. Use cut and paste rather than trying to retype the items by hand. Remember to leave the single quotes around the values of the keys in `twitterbot.py`

   * Copy "Consumer Key (API Key)" to be the value of `CONSUMER_KEY`
   * Copy "Consumer Secret (API Secret)" to be the value of `CONSUMER_SECRET`
   * Copy "Access Token" to be the value of `ACCESS_TOKEN`
   * Copy "Access Token Secret" to be the value of `ACCESS_TOKEN_SECRET`


**Step 3: Install Tweepy**

You'll need to install the tweepy package before you can use it.

1. Open a command line window and activate your FMS environment.
2. Run `conda install -c conda-forge tweepy`

Now you can import the tweepy library by adding `import tweepy` to the top of a `.py` file. The `twitterbot.py` file already includes this line for you.


**Step 4: Test the Bot**

The file `twitterbot.py` contains a minimum working example of a Twitter bot. Test the bot by typing `python twitterbot.py hello`. This should cause it to tweet a hello world message. If this works, then you are ready to go on to assignment 5.
