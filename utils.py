import re
import os
import praw
from dotenv import load_dotenv

load_dotenv()

def reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def extract_username(url):
    m = re.search(r"reddit\.com/user/([^/]+)/?", url)
    return m.group(1) if m else None

def fetch_user_data(username, limit=200):
    reddit = reddit_instance()
    redditor = reddit.redditor(username)
    comments = [(c.body, f"https://reddit.com{c.permalink}") for c in redditor.comments.new(limit=limit)]
    posts = [(p.title + "\n" + (p.selftext or ""), p.url) for p in redditor.submissions.new(limit=limit)]
    return comments, posts
