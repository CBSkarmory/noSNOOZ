#!/usr/bin/env python3
import time
import analytics
import os
import util
import contact

POST_DATABASE = "db.txt"


def post_db_contains(post_id):
    if not os.path.isfile(POST_DATABASE):
        return False

    lines = open(POST_DATABASE).readlines()
    for line in lines:
        if line.startswith("id: " + str(post_id)):
            return True
    return False


def write_to_file(posts):
    util.dout("Writing %d posts to post database" % len(posts))
    for post in posts:
        if not post_db_contains(post.id):
            db_file = open(POST_DATABASE, "a+")
            db_file.write(post_to_text(post))
            db_file.close()


def post_to_text(post):
    return "id: %s, title: %s, url: %s, score: %d\n" % \
           (post.id, post.title, post.url, post.score)


if __name__ == "__main__":
    running = True
    while running:
        time.sleep(2)

        # Query for predictions
        preds = analytics.public_get_predictions()
        write_to_file(preds)
