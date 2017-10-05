Programming Assignment 5: APIs and Twitterbots
==============================================
* Fundamentals of Modern Software - Fall 2017
* Due October 5 by 11:59 AM

Introduction
------------

The goals of the tasks that follow are:

1. To practice using third-party libraries to extend the capabilities of Python.
2. To explore using external web APIs.

In this assignment, you will add new functionality to the Twitter bot from lab. _**Before** starting work on this assignment, you should complete the process of setting up the Twitter bot. Refer to the file `setup.md` for detailed instructions._


**REMINDERS**

1. **When you are done, be sure to submit your work by pushing to GitHub.**
2. **You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.**
3. **Be sure to test your programs thoroughly on a wide range of inputs. We will.**
4. **Your programs' output should match the output in the samples EXACTLY, to the letter. We will grade your work in part using automated tests, and as you have seen, even a single-character difference in capitalization can cause a comparison not to match.**
5. **We have provided you with 'stub' programs that you can -- and should -- use as a starting point.**



twitterbot.py
----------

This file contains the hello world example from lab, plus stubs for three functions that you will need to implement. The file contains code which will launch one of four different functions depending on command-line arguments. To run it, type

    $ python twitterbot.py <mode>

where `<mode>` is `hello`, `random`, `secret`, or `custom`. Note that none of the modes produce any output on the command line. Instead, they do (or should, once you're done) cause the bot to post tweets on Twitter.

**1. Random Tweet Generator**

Implement the function `randomTweetGenerator` so that it generates and  random tweets. The stub version of the function draws on three `.txt` files provided with the assignment. Each tweet should take a random phrase from the first file, a random phrase from the second file, and a random hashtag from the third file, and combine them  to form a single string. Check out the timeline of [FMSBotTest](https://twitter.com/FMSBotTest) for some examples. (If you want, once you understand what is in these files, you can add lines to them for your own amusement. Doing so will not affect your grade on the assignment.)

Complete the function so that it sends out 10 random tweets each time the program is run.

You can find the Tweepy documentation on how to send a tweet here: <http://docs.tweepy.org/en/latest/api.html#API.update_status>.


**2. Secret Messages**

My friend ([FMSBotFriend](https://twitter.com/FMSBotFriend)) has been acting a little weird ... he or she keeps tweeting out cryptic messages with strange capitalization. Implement the function `secretMessage` so that it use Tweepy to get the twenty most recent tweets from a specified Twitter user, and stores them in a list. Then extract all of the _capitalized_ letters from the specified user's tweets, and concatenate them in reverse chronological order (i.e. as you read down in their timeline) to reveal a secret message. For example, if the user tweeted `hellO operator` at 12:06 and `the more you Know` at 12:05, then the mesage would be `OK`. Finish by tweeting out the secret message using Tweepy.

Get the username to watch from the command line as an additional parameter. For example:

    $ python twitterbot.py secret FMSBotFriend

You do not need to write the code that grabs the username; `twitterbot.py` passes the username as an argument to the `secretMessage` function that you will complete.

You can find the Tweepy documentation on how to pull in Tweets from a user's timeline here: <https://tweepy.readthedocs.io/en/v3.5.0/api.html#API.user_timeline>. (Hint: the tweets will be formatted as dictionaries. There is a specific entry in each dictionary that will contain the text of the tweet.)



**3. Custom Function**

Now it's your turn to add a feature of your own choosing to your Twitter bot. This is an open-ended task; you can extend the program in a way that's interesting to you.  The feature must use at least one function in the Tweepy library that you did not use in your solutions to the first two problems.

A few suggestions to start your ideation:

* Determine the current highest trending hashtag in two different places and tweet whether it is the same or different.
* Take two celebrities and report which of them has more followers on Twitter.
* Make the whole world hate you by bringing back [@StealthMountain](https://twitter.com/stealthmountain), which @ replied to users who said "sneak peak" to tell them they mean "sneak peek" instead.
* Use the Tweepy Streaming API to reply to mentions (other user tweets directed at your Twitter handle). For example, you could tell knock-knock jokes. If someone tags you in a tweet reading "Knock knock", @ reply them and tweet back, "Who's there?" Then if they @ reply with a name, tweet back "[name] who?"
* Integrate with another API that interests you (e.g. use NYC Open Data or the MTA to tweet about population trends or delayed subways).

You will get full credit for anything that works, as long as it uses a new Tweepy function.
