import pyotp
import sys

class TwoFactorAuthCLI:
    def __init__(self):
        self.secret_key = None

    def set_secret_key(self, secret_key):
        self.secret_key = secret_key

    def generate_2fa_code(self):
        if self.secret_key is None:
            print("Error: Secret key is not set")
            return
        totp = pyotp.TOTP(self.secret_key)
        otp_code = totp.now()
        print(f"2FA OTP: {otp_code}")

    def verify_2fa_code(self, input_code):
        if self.secret_key is None:
            print("Error: Secret key is not set")
            return False
        totp = pyotp.TOTP(self.secret_key)
        return totp.verify(input_code)

    def run(self):
        if len(sys.argv) > 1:
            self.secret_key = sys.argv[1]
        else:
            self.secret_key = pyotp.random_base32()
        print("Display Key: " + self.secret_key)
        while True:
            print("1. Generate 2FA Code")
            print("2. Verify 2FA Code")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.generate_2fa_code()
            elif choice == "2":
                input_code = input("Enter 2FA Code: ")
                if self.verify_2fa_code(input_code):
                    print("[✓] Valid OTP")
                else:
                    print("[X] Invalid OTP")
            elif choice == "3":
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    cli_app = TwoFactorAuthCLI()
    cli_app.run()
