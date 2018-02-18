#!/usr/bin/env python3
import praw, pdb, re, os, sys, pandas as pd

reddit = praw.Reddit("Gatherer")

sub = reddit.subreddit("news+worldnews")


def dout(message):
    print(f"[DEBUG] {message}")


def print_col(collection):
    for post in collection:
        print(f"Title: {post.title}")
        print(f"Text: {post.selftext}")
        print(f"Link: {post.url}")
        print(f"Score: {post.score}")
        print(f"Comments: {post.comments}")
        print("\n")


def get_top_hour_n(n):
    return sub.top(time_filter='hour',limit=n)


def get_rising_n(n):
    return sub.rising(limit=n)

#def get


if __name__ == "__main__":
    n= 10
    print_col(set(get_rising_n(n)) & set(get_top_hour_n(n)))
