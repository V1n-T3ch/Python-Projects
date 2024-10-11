import requests

def download_video(url, output_filename):
    response = requests.get(url)
    with open(output_filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded video as {output_filename}")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    output_filename = input("Enter the desired output filename (e.g., video.mp4): ")
    download_video(video_url, output_filename)