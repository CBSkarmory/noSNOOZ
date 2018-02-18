import smtplib
import sys
import util
import database
import handle_subscribers

EMAIL = "nosnoozhophacks18@gmail.com"
SENDER = "noSNOOZ"
SMP_MSG = "Hophacks 2018"
PASSW = lines = open("login.ini").readlines()[0]


TMOBILE = "@tmomail.net"
SPRINT = "@pm.sprint.com"
VERIZON = "@vtext.com"
ANT = "@mms.att.net"


MAX_MESSAGE_LENGTH = 155

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSW) # credentials as argument


def send_text(number, carrier, message):
    message = util.strip_non_ascii(message)
    server.sendmail(SENDER, number + carrier, message)
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
                util.dout("sent 1 txt")


def post_to_message(post):
    msg = []
    msg.append(post.shortlink)
    msg.append("\n")
    msg.append(str(post.score))
    msg.append(" pts, ")
    msg.append(str(util.post_age_min(post)))
    msg.append(" min ago")
    msg.append("\n")
    msg.append(post.title)
    return "".join(msg)

