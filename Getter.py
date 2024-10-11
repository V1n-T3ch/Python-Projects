import os
import urllib
import requests

def download_video(url, file_name):
    # Get the file name from the URL if it is not provided
    if file_name is None:
        file_name = urllib.parse.urlsplit(url).path.split('/')[-1]

    # Download the video from the URL
    response = requests.get(url, stream=True)

    # Check if the response is successful
    if response.status_code == 200:
        # Save the video to the file system
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f'Video downloaded successfully to {file_name}')
    else:
        print(f'Failed to download the video: {response.status_code}')

# Replace 'url' with the actual URL of the video
# Replace 'file_name' with the actual file name of the video if necessary
download_video('https://www.xnxx.com/video-1aogu3cc/quickie_fuck_session_with_stepmom_and_stepsis', 'FTS.mkv')