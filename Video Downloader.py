import requests
from pytube import YouTube

def download_video(url):
    if "youtube.com" in url:
        # For YouTube videos
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f"Downloaded: {yt.title}")
    else:
        # For non-YouTube sites
        response = requests.get(url)
        with open("video.mp4", 'wb') as file:
            file.write(response.content)
        print("Downloaded video")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)