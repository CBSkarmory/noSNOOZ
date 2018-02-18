import smtplib
import sys
import time

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
server.login(EMAIL, sys.argv[1])

def send_text(number, carrier, message):
    server.sendmail(EMAIL, number + carrier, message);
    print("Sending message...")

def get_carrier(ans):
    ans.upper();
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

while(True):
    time.sleep(1)

    # Receive and sanitize phone number
    phone_input = str(input("Enter your phone number\n"))
    phone_number = sanitize_number(phone_input)
    if not phone_number:
        continue

    # Receive and sanitize carrier
    carrier_input = input("Enter your carrier\n")
    carrier = get_carrier(carrier_input)
    if carrier == "FAIL":
        continue

    subscribers_file = open("subscribers.txt", "a+")
    subscribers_file.write(phone_number + " " + carrier)
    subscribers_file.close()

    # Receive and sanitize message
    msg_input = input("Enter message\n")
    msg_len = MAX_MESSAGE_LENGTH - len(EMAIL) - len(phone_number) - len(carrier)
    message = msg_input[0:msg_len]

    # Send message
    send_text(phone_number, carrier, message)
