#!/usr/bin/python

import praw
import re

reddit = praw.Reddit('wholesome_booty')

subreddit = reddit.subreddit('me_irl')


# subreddit.submit(
#     'Colorado has more Subarus',
#     'Title says all')


for submission in subreddit.hot(limit=5):
    for top_level_comment in submission.comments:
        print(top_level_comment.body)
        if re.search("me too thanks", top_level_comment.body, re.IGNORECASE):
            top_level_comment.reply("Me 3 thx <3")
            print top_level_comment.body
            # comments.append(tb(top_level_comment.body))
            # print "We would reply to: " + top_level_comment.body


    # if re.search("me too thanks", submission.title, re.IGNORECASE):
    #     submission.reply("Size doesn't matter. It's about the passion.")
    #     print "Bot replying to: " + submission.title
