from pytube import YouTube

url = input("Enter the video URL: ") # Replace 'YOUR_VIDEO_ID' with the actual video ID

yt = YouTube(url)

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()