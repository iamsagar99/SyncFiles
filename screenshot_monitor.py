import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ftplib import FTP
from dotenv import load_dotenv

# Load configs
load_dotenv()

SCREENSHOT_DIR = os.getenv("SCREENSHOT_DIR")
FTP_HOST = os.getenv("FTP_HOST")
FTP_PORT = int(os.getenv("FTP_PORT"))
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")

# get start time 
start_time = time.time()

def get_latest_file(directory, extension=".png"):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension) and not f.startswith('.')]
    if not files:
        return None
    return max(files, key=os.path.getctime)

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".png") and not os.path.basename(event.src_path).startswith('.'):
            file_creation_time = os.path.getctime(event.src_path)
            if file_creation_time > start_time:
                print(f"New screenshot detected: {event.src_path}")
                latest_file = get_latest_file(SCREENSHOT_DIR)
                if latest_file:
                    self.upload_to_ftp(latest_file)

    def upload_to_ftp(self, file_path):
        try:
            with FTP() as ftp:
                ftp.connect(FTP_HOST, FTP_PORT)
                ftp.login(FTP_USER, FTP_PASS)
                with open(file_path, "rb") as file:
                    ftp.storbinary(f"STOR {os.path.basename(file_path)}", file)
                print(f"Uploaded: {file_path}")
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")

if __name__ == "__main__":
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, SCREENSHOT_DIR, recursive=False)
    observer.start()

    print("Monitoring for new screenshots...")
    try:
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
