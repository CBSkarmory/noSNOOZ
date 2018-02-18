# utilities file
import praw
import sys
import time

DEBUG = True

def dout(message):
    if DEBUG:
        print(f"[DEBUG] {message}")


def err(error_code, error_message):
    print(f"[ERROR] {message}")
    sys.exit(error_code)


# seconds since epoc
def current_sec_time():
        return int(round(time.time()))


def post_age_sec(post):
    return int(current_sec_time() - post.created_utc)


def post_age_min(post):
    return post_age_sec(post) / 60


# prints info about each post in the collection to stdout
def print_col(collection):
    for post in collection:
        print(f"Title: {post.title}")
        print(f"Text: {post.selftext}")
        print(f"Link: {post.url}")
        print(f"Score: {post.score}")
        print(f"top-lv com: {len(post.comments)}")
        print(f"seconds elapsed: {(current_sec_time()) - post.created_utc}")
        print("\n")
