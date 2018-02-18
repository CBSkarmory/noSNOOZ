import os
import util

PIPE = "js_to_py.txt"


def add_subscriber_to_db(phone_number):
    file = open("subscribers.txt", "w+")
    file.write(phone_number + "\n")
    file.close()


# invoke from node.js server
# expected input format:
#
# BEGIN FILE
# 5555555555:ANT:news,worldnews
# END FILE
#
if __name__ == "__main__":
    if not os.path.isfile(PIPE):
        util.err(500, "internal pipe file not found")
    with open(PIPE, "r") as f:
        line = f.readline()
        data = line.split(":")
        subs = data[2].split(",")