import time
import scr
import os

FILE_NAME = "db.txt"

def fileContains(post_id):
    if not os.path.isfile(FILE_NAME):
        return False

    lines = open(FILE_NAME).readlines()
    for line in lines:
        if line.startswith("id: " + str(post_id)):
            return True
    return False

def writeToFile(posts):
    print("Writing %d posts to file" % len(posts))
    for post in posts:
        if not fileContains(post.id):
            db_file = open(FILE_NAME, "a+")
            db_file.write(postToText(post))
            db_file.close()


def postToText(post):
    return "id: %s, title: %s, url: %s, score: %d\n" % \
           (post.id, post.title, post.url, post.score)

while (True):
    time.sleep(2)

    # Query for predictions
    posts = scr.public_get_predictions()

    writeToFile(posts)
