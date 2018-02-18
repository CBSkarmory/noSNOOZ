#!/usr/bin/env python3
import os
import util

PIPE = "js_to_py.txt"

SUBSCRIBER_DB = "subscribers.txt"


def add_subscriber(phone_number, carrier, subs):
    util.dout(f"adding subscriber XXX-XXX-{phone_number % 1000} to subscriber database")
    file = open(SUBSCRIBER_DB, "w+")
    file.write(f"{phone_number}:{carrier}:{subs}\n")
    file.close()


# returns list of strings
# string formatting:
# 5555555555:ANT
def get_subscriber_data():
    lines = open(SUBSCRIBER_DB).readlines()
    data = []
    for l in lines:
        fields = l.split(":")
        data.append(f"{fields[0]}:{fields[1]}")
    return data


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

        add_subscriber(int(data[0]), data[1], data[2])
