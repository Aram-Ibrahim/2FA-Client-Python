import time
import pyotp
import sys
import qrcode

qrCode_save_fileName="2FA_totp"+".png"

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

time_based_otp=pyotp.TOTP(args_key).provisioning_uri(name="SayanDasgupta",
                                                     issuer_name="Cadris_App_Example")


print("Display_Key: "+args_key)
print("uri: "+time_based_otp)
qrcode.make(time_based_otp).save(qrCode_save_fileName)
