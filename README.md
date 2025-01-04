# FileSync - Seamless File Transfer Across Devices 📱💻

This project provides a simple solution to transfer files between devices using FTP. Whether you're working on a Mac, Windows, or Linux, this tool automatically uploads files (like screenshots or any other type) from your computer to your Android device. It’s a hassle-free way to sync files across devices without needing cables or manual transfers.

---

### 🚀 **How It Works**
1. **Capture Files on Your Computer**: Whether it's a screenshot, document, or any file type, simply create or save it on your computer.
2. **Automatic Syncing**: The file is automatically uploaded to a folder on your Android device via FTP.
3. **Stay Organized**: No more manual file transfers or dealing with messy cables.

---

### 🔧 **Technologies Used**
- **FTP**: For transferring files between your computer and Android device.
- **Python**: The backend logic to manage file transfers and automation.
- **Watchdog**: Monitors your computer for new files and triggers the transfer to Android.

---

### 🛠️ **How to Use**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iamsagar99/SyncFiles.git
   cd SyncFiles
   ```

2. **Run the Script on Your Computer**:
   Update the FTP credentials in the `ftp_server.py` file and then run the script:
   ```bash
   python ftp_server.py && python screenshot_monitor.py
   ```

   The script will start monitoring the folder where your files are created (such as the screenshot folder) and automatically upload new files to your Android device.

3. **Run the FTP Client on Android**:
   Download **Termux** on your Android device and install Python. Then, add the `ftp_client.py` file to your directory and run the following command:
   ```bash
   python ftp_client.py
   ```

   Your files will be available in the folder you've specified on your Android device.

---

### 🤔 **What Drives Me to Build This**

I was watching a class recording and taking notes on my Android tablet. I found myself spending too much time recreating tables and charts that were already in the video. That's when I thought: why not automate this?

So, I built a simple FTP server to automatically transfer screenshots and other files from my Mac to my Android tablet. It turned out to be a huge time-saver, and I wanted to make this solution available to others who might be facing similar issues.

---

### 🌐 **For All Devices on the Same Network**
This project isn’t limited to just Mac or Android. If you’re using any device that supports FTP (Windows, Linux, etc.), you can use this tool to share files across devices on the same network. Whether you need to sync documents, images, or anything else, FileSync makes it simple and efficient.

Now, you can effortlessly transfer files from one device to another with just a few lines of code and minimal setup!