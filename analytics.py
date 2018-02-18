#!/usr/bin/env python3
import praw
import pandas as pd
import numpy as np
import util

reddit = praw.Reddit("Gatherer")

sub = reddit.subreddit("news+worldnews")

DEBUG = True


def get_top_hour_n(n):
    return sub.top(time_filter='hour',limit=n)


def get_hot_n(n):
    return sub.hot(limit=n)


def get_rising_n(n):
    return sub.rising(limit=n)


# gets the maximum score from a group of comments
def max_score(comments):
    max_val = 0
    for com in comments.list():
        if isinstance(com, praw.models.MoreComments):
            continue
        max_val = max(max_val, com.score)
    return max_val

# gives back posts as dataframe holding useful stats
def posts_as_df(posts):
    df = pd.DataFrame({
        'post': [post for post in posts]
    })
    df['score'] = df.post.apply(lambda post: post.score)
    df['top_lv_c'] = df.post.apply(lambda post: len(post.comments))
    df['seconds_old'] = df.post.apply(util.post_age_sec)
    df['max_c_score'] = df.post.apply(lambda post: max_score(post.comments))
    # these are times 1000
    df['dp_dt'] = (df.score * 1000.0 * 60.0 / df.seconds_old).apply(int)
    df['d2p_dt2'] = (df.dp_dt * 60.0 / df.seconds_old).apply(int)
    return df


# gets predictions for posts that will get front page
# current algorithm checks for posts in the intersection set with 1st or 2nd derivative 2 sdev above mean for intersect
# intersection set is the intersection for top n rising and top(hour)
def public_get_predictions(): #TODO modify algo to check for min time
    n = 2.0
    df = posts_as_df(set(get_rising_n(8)) & set(get_top_hour_n(8)))
    df_filtered = df[(( (df.dp_dt - np.mean(df.dp_dt)) > ( n * np.std(df.dp_dt) )) |
               ( (df.dp_dt - np.mean(df.d2p_dt2)) > ( n * np.std(df.d2p_dt2) )))]
    return df_filtered['post']


# prints interesting info
def print_hot_vs_intersection():
    print("hot")
    print(posts_as_df(get_hot_n(5)))
    print("intersect")
    print(posts_as_df(set(get_rising_n(8)) & set(get_top_hour_n(8))))

if __name__ == "__main__":
    # do whatever, don't call this as main
    print_hot_vs_intersection()
