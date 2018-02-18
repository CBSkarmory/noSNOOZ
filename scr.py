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

# # 3 level deep sum of top comments
# def sum3(post):
#     return comment_sum(post.comments, 3)

# def comment_sum(comment_forest, levels):
#     if levels == 0:
#         return 0
#     val, idx = get_max_pos(comment_forest)
#     return val + comment_sum(comment_forest[idx], levels - 1)
    
# def get_max_pos(comment_forest):
#     max_val = -1
#     max_idx = -1
#     for i in range(len(comment_forest)):
#         if comment_forest[i].score > max_val:
#             max_val = comment_forest[i].score
#             max_idx = i
#     return (max_val, max_idx)

def max_score(comments):
    max_comment = None
    max_score = 0
    for com in comments.list():
        if com.score > max_score:
            max_score = com.score
            max_comment = com
    return max_score
    

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
