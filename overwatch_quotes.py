import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('overwatch')

# Reads Top 5 stories in 'Hot' category of /r/Overwatch
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to =[]
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
