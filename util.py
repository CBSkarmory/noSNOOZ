# utilities file
import sys

DEBUG = True

def dout(message):
    if DEBUG:
        print(f"[DEBUG] {message}")

def err(error_code, error_message):
    print(f"[ERROR] {message}")
    sys.exit(error_code)