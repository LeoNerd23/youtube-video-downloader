import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

url = "insert the video url here"

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Downloading: {yt.title}")

desktop = Path.home() / "Desktop"
download_folder = desktop / "youtube-video-downloader"
download_folder.mkdir(exist_ok=True)

ys = yt.streams.get_highest_resolution()
ys.download(output_path=download_folder)

print(f"Download complete! The video was saved in: {download_folder}")
