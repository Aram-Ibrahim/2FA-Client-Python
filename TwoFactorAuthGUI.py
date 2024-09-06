import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, filedialog
import cv2
import pyzbar.pyzbar as pyzbar
import pyotp

class TwoFactorAuthGUI:
    def __init__(self):
        self.window = ctk.CTk()  
        self.window.title("Two-Factor Authentication Client")
        self.window.geometry("400x425")
        ctk.set_appearance_mode("dark")  
        self.window.resizable(False, False) 

        self.scan_qr_button = ctk.CTkButton(self.window, text="Select QR Code Image", command=self.scan_qr_code, font=(None,20))
        self.scan_qr_button.pack(pady=10)
        
        self.or_label = ctk.CTkLabel(self.window, text="or",font=(None,30))
        self.or_label.pack(pady=10)
        
        self.key_label = ctk.CTkLabel(self.window, text="Enter Secret Key:",font=(None,20))
        self.key_label.pack(pady=10)

        self.key_entry = ctk.CTkEntry(self.window, width=200, height=30,font=(None,20))
        self.key_entry.pack()

        self.generate_button = ctk.CTkButton(self.window, text="Generate 2FA Code", command=self.generate_2fa_code, font=(None,20))
        self.generate_button.pack(pady=10)

        self.code_frame = ctk.CTkFrame(self.window, corner_radius=10, width=300, height=200)
        self.code_frame.pack(fill="x",pady=20,padx=10)
        
        self.otp_label = ctk.CTkLabel(self.code_frame , text="2FA OTP:",font=(None,20))
        self.otp_label.pack(pady=10)

        self.otp_value_label = ctk.CTkLabel(self.code_frame , text="", font=(None,20))
        self.otp_value_label.pack(pady=10)

        self.copy_btn = ctk.CTkButton(self.code_frame , text="Copy", command=lambda: self.copy_to_clipboard(self.otp_value_label.cget("text")),font=(None,20))
        self.copy_btn.pack(pady=10)

        self.secret_key = None

    def scan_qr_code(self):
        file_path = filedialog.askopenfilename(title="Select QR Code Image", filetypes=[("Image Files", ".png .jpg .jpeg")])
        if file_path:
            try:
                img = cv2.imread(file_path)
                detector = cv2.QRCodeDetector()
                data, points, _ = detector.detectAndDecode(img)
                if points is not None:
                    self.secret_key = data
                    self.key_entry.delete(0, tk.END)
                    self.key_entry.insert(0, self.secret_key)
                else:
                    print("Error: Unable to detect QR code in image")
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Error: No file selected")

    def generate_2fa_code(self):
        if self.key_entry.get() is None:
            print("Error: Secret key is not set")
            return
        totp = pyotp.TOTP(self.key_entry.get())
        otp_code = totp.now()
        self.otp_value_label.configure(text=otp_code)

    def copy_to_clipboard(self, text):
        self.window.clipboard_clear()
        self.window.clipboard_append(text)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui_app = TwoFactorAuthGUI()
    gui_app.run()
