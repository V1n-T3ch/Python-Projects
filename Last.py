import requests

chunk_size=1024

url = input("Enter the video url: ")

r =requests.get(url, stream=True)

with open("FTS.mp4", "wb") as f:
	for chunk in r.iter_content(chunk_size=chunk_size):
		f.write(chunk)