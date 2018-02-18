


def addSubscriberToDb(phone_number):
    file = open("subscribers.txt", "w+")
    file.write(phone_number + "\n")
    file.close()




