import os

import requests
import yt_dlp
import instaloader
from moviepy import AudioFileClip

# Set up the download folder
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# FFmpeg location path (ensure this matches your actual installation path)
FFMPEG_PATH = r'C:\ffmpeg\bin\ffmpeg.exe'  # Update with your FFmpeg path

# Function to download YouTube video and convert it to MP3
def download_youtube_to_mp3(link):
    try:
        print("Fetching YouTube video...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'ffmpeg_location': FFMPEG_PATH  # Force using the correct FFmpeg path
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download and conversion successful!")
    except Exception as e:
        print("❌ Error downloading YouTube video:", e)

# Function to download Instagram reel and convert it to MP3
def download_instagram_reel_to_mp3(link):
    try:
        print("Fetching Instagram Reel...")
        loader = instaloader.Instaloader()
        shortcode = link.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        if not post.video_url:
            raise ValueError("❌ This Instagram post does not contain a video.")

        video_url = post.video_url
        video_path = os.path.join(DOWNLOAD_FOLDER, f"{shortcode}.mp4")

        # Download video using requests
        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            with open(video_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
        else:
            raise ValueError("❌ Failed to download Instagram reel.")

        mp3_file = os.path.splitext(video_path)[0] + ".mp3"

        # Convert to MP3 using MoviePy
        audio = AudioFileClip(video_path)
        audio.write_audiofile(mp3_file)
        audio.close()
        os.remove(video_path)

        print("✅ Conversion successful! MP3 file saved at:", mp3_file)
    except Exception as e:
        print("❌ Error downloading or converting Instagram Reel:", e)

# Menu to choose a platform
def main():
    while True:
        print("\nChoose an option:")
        print("1. Convert YouTube to MP3")
        print("2. Convert Instagram Reel to MP3")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            youtube_link = input("Enter the YouTube video link: ")
            download_youtube_to_mp3(youtube_link)
        elif choice == "2":
            instagram_link = input("Enter the Instagram Reel link: ")
            download_instagram_reel_to_mp3(instagram_link)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
