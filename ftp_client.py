import os
from ftplib import FTP
import time

# FTP server credentials
FTP_HOST = "192.168.0.100" # Change this to your FTP server's IP address, the value of FTP_HOST in ftp_server.py
FTP_PORT = 2121
FTP_USER = "username" # Change this to your FTP user's username, the value of FTP_USER in ftp_server.py
FTP_PASS = "password" # Change this to your FTP user's password, the value of FTP_PASS in ftp_server.py

# Directory to save downloaded files
SAVE_DIR = os.path.expanduser("~/storage/dcim/CapCut") # I am syncing this in termux

def ensure_save_directory():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR, exist_ok=True)
        print(f"Created directory: {SAVE_DIR}")
    else:
        print(f"Save directory exists: {SAVE_DIR}")

def download_screenshots():
    try:
        with FTP() as ftp:
            ftp.connect(FTP_HOST, FTP_PORT)
            ftp.login(FTP_USER, FTP_PASS)
            files = ftp.nlst() 

            for file in files:
                local_path = os.path.join(SAVE_DIR, file)
                if not os.path.exists(local_path):
                    with open(local_path, "wb") as f:
                        ftp.retrbinary(f"RETR {file}", f.write)
                    print(f"Downloaded: {file}")
                else:
                    print(f"File already exists: {file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ensure_save_directory()
    print("Listening for new screenshots...")
    while True:
        download_screenshots()
        time.sleep(10) 
