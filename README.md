# 🎵 YouTube & Instagram to MP3 Converter  

## 📌 Project Overview  
This Python-based application allows users to convert YouTube and Instagram videos into MP3 audio files. By providing a video link, the system downloads the video, extracts the audio, and saves it in MP3 format. The project utilizes popular Python libraries and **FFmpeg** software for efficient audio processing.  

## ✨ Features  
✅ **YouTube to MP3 Conversion** – Downloads and extracts high-quality audio from YouTube videos.  
✅ **Instagram to MP3 Conversion** – Supports downloading and extracting audio from Instagram videos.  
✅ **Automated Processing** – Streamlines video downloading, conversion, and file management.  
✅ **Efficient File Handling** – Uses FFmpeg and `moviepy` for high-quality audio extraction.  

## 🛠️ Tech Stack & Libraries Used  
- **Python** – Core programming language.  
- `yt_dlp` – Downloads videos from YouTube efficiently.  
- `instaloader` – Fetches Instagram videos.  
- `requests` – Handles web requests for fetching media.  
- `moviepy` – Converts video files into MP3 audio.  
- `os` – Manages file handling and system operations.  
- **FFmpeg** – Essential for high-quality audio extraction and conversion.  

## 🔧 How It Works  
1. **Provide a YouTube or Instagram video link**.  
2. The application **downloads** the video using `yt_dlp` (YouTube) or `instaloader` (Instagram).  
3. The video file is processed using **FFmpeg** and `moviepy` to **extract the audio**.  
4. The extracted audio is **saved in MP3 format** in the specified directory.  
5. The user can then access and play the MP3 file.  

## 📦 Installation  
1. **Clone the repository**  
   ```sh
   git clone https://github.com/Arth210501/Python_MP4_to_MP3.git
   cd Python_MP4_to_MP3
