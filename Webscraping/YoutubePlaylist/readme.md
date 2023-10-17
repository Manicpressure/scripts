# YouTube Playlist Downloader (MP3)

Download an entire YouTube playlist as MP3 files.
Dependencies:
```
    pytube
    moviepy
```

You can install these dependencies via pip:

`pip install pytube moviepy`

Usage:
`python3 YoutubePlaylistDownloaderMP3.py [SAVE_PATH] [PLAYLIST_URL]`

SAVE_PATH: The directory path where you want the downloaded MP3 files to be saved.
PLAYLIST_URL: The full URL of the YouTube playlist you wish to download.

Example:
`python3 YoutubePlaylistDownloaderMP3.py /home/user/Downloads https://www.youtube.com/playlist?list=PLEiXLyRdrYnbM1eP6Kd8HVsc_lKCUACkM`

Features:
    - Sanitized Filenames: Removes special characters and extra spaces from video titles to create safe filenames.
    - Error Handling: In case of download errors, the script will retry up to three times before skipping to the next video.
    - Age Restriction Check: If a video in the playlist is age-restricted, the script will log it and continue with the next video.
    - Existing File Check: The script checks for already downloaded files in the destination directory and skips them.
