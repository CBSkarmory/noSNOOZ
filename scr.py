#!/usr/bin/env python3
import praw, pdb, re, os, sys, pandas as pd, time

reddit = praw.Reddit("Gatherer")

sub = reddit.subreddit("news+worldnews")

DEBUG = True


def dout(message):
    if DEBUG:
        print(f"[DEBUG] {message}")


def current_sec_time():
    return int(round(time.time()))        


def print_col(collection):
    for post in collection:
        print(f"Title: {post.title}")
        print(f"Text: {post.selftext}")
        print(f"Link: {post.url}")
        print(f"Score: {post.score}")
        print(f"top-lv com: {len(post.comments)}")
        print(f"seconds elapsed: {(current_sec_time()) - post.created_utc}")
        print("\n")


def get_top_hour_n(n):
    return sub.top(time_filter='hour',limit=n)


def get_rising_n(n):
    return sub.rising(limit=n)


def max_score(comments):
    max_val = 0
    for com in comments.list():
        max_val = max(max_val, com.score)
    return max_val
    

def get_top_hr_as_df(n):
    top_n = get_top_hour_n(n)
    df = pd.DataFrame({
        'post': [post for post in top_n]
    })
    df['score'] = df.post.apply(lambda post: post.score)
    df['top_lv_c'] = df.post.apply(lambda post: len(post.comments))
    df['seconds_old'] = df.post.apply(lambda post: int(current_sec_time() - post.created_utc))
    df['max_c_score'] = df.post.apply(lambda post: max_score(post.comments))
    return df


if __name__ == "__main__":
    n= 7
    #print_col(set(get_rising_n(n)) & set(get_top_hour_n(n)))
    print(get_top_hr_as_df(5))
