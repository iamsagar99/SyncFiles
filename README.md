# Screenshot Sync - Seamless Screenshot Transfer from Mac to Android 📸📱

This project is a simple solution to transfer screenshots from your Mac to your Android device using FTP. Whenever you take a screenshot on your Mac, it will be automatically uploaded to a specific directory on your Android device, making it easier to access your files without manual transfers.

---

### 🚀 **How It Works**
1. **Capture Screenshots on Your Mac**: Simply take a screenshot on your Mac.
2. **Automatic Syncing**: The screenshot is automatically uploaded to a folder on your Android device via FTP.
3. **Stay Organized**: No more manual file transfers or searching through cluttered folders.

---

### 🔧 **Technologies Used**
- **FTP**: For transferring files between your Mac and Android device.
- **Python**: Used for the backend logic to manage the file transfers.
- **Watchdog**: To monitor your Mac for new screenshots and trigger the transfer.

---

### 🛠️ **How to Use**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iamsagar99/SyncFiles.git
   cd SyncFiles
   ```

2. **Run the Script on Your Mac**:
   Update the FTP credentials in the `ftp_server.py` file and then run the script:
   ```bash
   python ftp_server.py && python screenshot_monitor.py
   ```

   The script will start monitoring your screenshots folder and will automatically upload new screenshots to your Android device.

3. **Run the FTP Client on Android**:
   Download termux and install python on it. And just add `ftp_client.py` on your directory run the command:
    ```bash
   python ftp_client.py
   ```
    the screenshots will be available in the folder you've specified.

---

### 🤔 **What Drives Me to Build This**

I was watching a class recording and taking notes on my Android tablet. I found myself spending too much time recreating tables and charts that were already in the video. That’s when I thought, why not automate this?

So, I built a simple FTP server to automatically transfer whatever screenshots I take on my Mac to my Android tablet. This project made my workflow much more efficient, and I hope it can do the same for you!

---

Now, you can take screenshots on your Mac, and they’ll be automatically transferred to your Android device!