# 📥 YouTube Content Downloader

![Banner](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![yt-dlp](https://img.shields.io/badge/yt--dlp-v2024.10.24-yellow?style=for-the-badge&logo=youtube)
![ffmpeg](https://img.shields.io/badge/ffmpeg-Installed-green?style=for-the-badge&logo=ffmpeg)

## 🌟 Introduction
YouTube Content Downloader is a Python-based tool that allows you to download various types of content from YouTube channels. It supports **shorts**, **live videos**, **playlists**, and **all video uploads**. This tool provides an easy-to-use console interface to input your desired channel, content type, and handle any restrictions.

## 🎨 Features
- **Download YouTube Shorts**: Automatically filters and downloads videos that are 60 seconds or less.
- **Download Live Videos**: Filter and download live stream recordings from a channel.
- **Download Playlists**: Easily grab all videos from a specific playlist.
- **Download All Content**: Download all available videos from a channel in the best available quality.
- **Handles Age-Restricted Content** with cookie support.

## 🛠️ How It Works
The tool uses the `yt-dlp` library to extract and download videos based on the user's chosen content type. It also leverages `ffmpeg` to merge video and audio formats for high-quality output.

### 📑 Script Breakdown
1. **User Input**: Prompts the user to enter the channel username and select the type of content to download.
2. **Content Type Filtering**: Sets up filters based on the content type, such as shorts (less than 60 seconds), live videos, or playlists.
3. **Custom Folder Structure**: Downloads are organized into appropriate subfolders based on content type.
4. **Cookie-Based Authentication**: Optionally supports a cookie file for downloading age-restricted content.
5. **Resolution and Quality**: The tool downloads videos in the maximum resolution compatible with mobile viewing.

## 🚀 Getting Started

### 📝 Prerequisites
- **Python 3.8+** installed on your system.
- **yt-dlp** Python library installed. You can install it using:
  ```bash
  pip install yt-dlp
ffmpeg installed and added to your system's environment variables.

📂 Directory Structure
📦YourProjectFolder
 ┃ 📜ffmpeg.exe
 ┣ 📂vid
 ┣ 📜cookies.txt
 ┣ 📜main.py
 ┗ 📜README.md
🛠️ Installation
Clone this repository:

git clone https://github.com/yourusername/YouTube-Content-Downloader.git
cd YouTube-Content-Downloader
Install the required dependencies:

pip install -r requirements.txt
Ensure ffmpeg is installed and accessible via your system’s PATH or specify its location in the script.

💻 Usage
Run the Script:

python main.py
Input Prompts:

Enter the YouTube channel username (e.g., @imhecate).
Choose the content type:
1 for Shorts
2 for Live
3 for Playlist
4 for All
Handle Age-Restricted Content:

If you have a cookie file, provide the file path to access age-restricted videos.
📋 Example
Enter the YouTube channel username (e.g., @imhecate): @ConFilm
Select content type to download:
1. Shorts
2. Live
3. Playlist
4. All (All video content)
Enter the number (1-4) corresponding to your choice: 1
Do you have a cookies file for age-restricted videos? (y/n): n
Downloading content (shorts) from: https://www.youtube.com/@ConFilm
🖥️ Requirements
Python 3.8+
yt-dlp v2024.10.24+
ffmpeg installed and configured in your system's PATH
🛡️ Troubleshooting
ffmpeg not installed error: Ensure that ffmpeg is properly installed and its path is correctly added to your system's PATH.
Invalid YouTube channel: Ensure that you provide the correct channel username (starting with @).
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Created with ❤️ by Hecate. Contributions, issues, and feature requests are welcome!
