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

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, sys.argv[1])

def send_text(number, carrier, message):
    msg_len = 155 - len(EMAIL + number + carrier)
    message = message[0:msg_len]
    if len(number) == 10 and carrier != "FAIL":
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

while(True):
    num = input("Enter your phone number\n")
    car = input("Enter your carrier\n")
    msg = input("What message?\n")
    carrier = get_carrier(car)
    send_text(num, carrier, msg)
    time.sleep(1)

