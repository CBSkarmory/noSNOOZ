import smtplib
import sys
import util
import database
import handle_subscribers

EMAIL = "nosnoozhophacks18@gmail.com"
SENDER = "noSNOOZ"
SMP_MSG = "Hophacks 2018"

TMOBILE = "@tmomail.net"
SPRINT = "@pm.sprint.com"
VERIZON = "@vtext.com"
ANT = "@mms.att.net"

MAX_MESSAGE_LENGTH = 155

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, "hophacks18") # credentials as argument


def send_text(number, carrier, message):
    message = util.strip_non_ascii(message)
    server.sendmail(EMAIL, number + carrier, message)
    print("Sending message...")


def get_carrier(ans):
    ans.upper()
    if ans == "TMOBILE":
        return TMOBILE
    elif ans == "SPRINT":
        return SPRINT
    elif ans == "VERIZON":
        return VERIZON
    elif ans == "ANT":
        return ANT
    else:
        return "FAIL"


def sanitize_number(phone_number):
    phone_number = phone_number.replace("-", "")
    if len(phone_number) == 10 and phone_number.isdigit():
        return phone_number
    else:
        return False


def send_notif_excl_dup(posts):
    for p in posts:
        notification = post_to_message(p)
        if not database.post_db_contains(p.id):
            subscriber_data = handle_subscribers.get_subscriber_data()
            for entry in subscriber_data:
                data = entry.split(":")
                p_num = data[0]
                p_carrier = get_carrier(data[1])
                send_text(p_num, p_carrier, notification)


def post_to_message(post):
    msg = []
    msg.append(post.url)
    msg.append("\n")
    msg.append(str(post.score))
    msg.append(" points, ")
    msg.append(str(util.post_age_min(post)))
    msg.append(" min ago")
    msg.append("\n")
    msg.append(post.title)
    return "".join(msg)

#TODO disable all of below
#while True:
#    time.sleep(1)

#    # Receive and sanitize phone number
#    phone_input = str(input("Enter your phone number\n"))
#    phone_number = sanitize_number(phone_input)
#    if not phone_number:
#        continue

#    # Receive and sanitize carrier
#    carrier_input = input("Enter your carrier\n")
#    carrier = get_carrier(carrier_input)
#    if carrier == "FAIL":
#        continue

#    subscribers_file = open("subscribers.txt", "a+")
#    subscribers_file.write(phone_number + " " + carrier)
#    subscribers_file.close()

#    # Receive and sanitize message
#    msg_input = input("Enter message\n")
#    msg_len = MAX_MESSAGE_LENGTH - len(EMAIL) - len(phone_number) - len(carrier)
#    message = msg_input[0:msg_len]

#    # Send message
#    send_text(phone_number, carrier, message)
