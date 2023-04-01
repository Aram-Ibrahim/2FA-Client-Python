import time
import pyotp
import sys

def optionalLoader(primary, pos, secondary) :
    ret=""
    try:
            if (pos>-1) :
                ret = primary[pos]
            else:
                ret = primary
    except:
          ret = secondary
    return ret

def input_otp_verification(time_based_otp):
    input_code=input("Enter 2FA Code: ")
    return time_based_otp.verify(input_code)

args_key = optionalLoader(sys.argv, 1, pyotp.random_base32())

time_based_otp=pyotp.TOTP(args_key)


print("Display_Key: "+args_key)
print("2FA OTP: "+time_based_otp.now())

isValid=False

isValid = input_otp_verification(time_based_otp)
if(isValid):
    print("[✓] Valid OTP")
else:
    print("[X] Invalid OTP")
