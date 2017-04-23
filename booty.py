#!/usr/bin/python

import praw
import re

reddit = praw.Reddit('wholesome_booty')

subreddit = reddit.subreddit('renosubaru')

# subreddit.submit(
#     'Colorado has more Subarus',
#     'Title says all')

for submission in subreddit.hot(limit=5):
    if re.search("colorado", submission.title, re.IGNORECASE):
        submission.reply("Size doesn't matter. It's about the passion.")
        print "Bot replying to: " + submission.title
