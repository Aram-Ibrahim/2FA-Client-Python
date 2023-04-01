import time
import pyotp
import sys

key = sys.argv[1]

totp=pyotp.TOTP(key)

print("Display_Key: "+key)

while True:
    print(totp.verify(input("Enter OTP: ")))

