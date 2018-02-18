#!/usr/bin/env python3
import time
import analytics
import os

FILE_NAME = "db.txt"


def file_contains(post_id):
    if not os.path.isfile(FILE_NAME):
        return False

    lines = open(FILE_NAME).readlines()
    for line in lines:
        if line.startswith("id: " + str(post_id)):
            return True
    return False


def write_to_file(posts):
    print("Writing %d posts to file" % len(posts))
    for post in posts:
        if not file_contains(post.id):
            db_file = open(FILE_NAME, "a+")
            db_file.write(post_to_text(post))
            db_file.close()


def post_to_text(post):
    return "id: %s, title: %s, url: %s, score: %d\n" % \
           (post.id, post.title, post.url, post.score)


if __name__ == "__main__":
    while True:
        time.sleep(120)

        # Query for predictions
        posts = analytics.public_get_predictions()

        write_to_file(posts)
