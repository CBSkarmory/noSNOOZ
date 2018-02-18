

def add_subscriber_to_db(phone_number):
    file = open("subscribers.txt", "w+")
    file.write(phone_number + "\n")
    file.close()



