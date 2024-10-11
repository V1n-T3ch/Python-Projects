import youtube_dl

def download_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save video with its title as the filename
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    download_video(video_url)
