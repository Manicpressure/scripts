import re
import os
import argparse
from pytube import YouTube, Playlist
from pytube.exceptions import AgeRestrictedError
import moviepy.editor as mp

def sanitize_filename(filename):
    """Sanitize filenames to remove special characters and extra spaces."""
    return re.sub(r'[^\w\s-]', '', filename).strip()

def download_as_mp3(video, save_path):
    """Download a single YouTube video as an MP3."""
    sanitized_title = sanitize_filename(video.title)
    
    # Extract audio stream
    stream = video.streams.filter(only_audio=True, file_extension="mp4").first()

    # Download the audio stream
    mp4_path = stream.download(output_path=save_path, filename=sanitized_title)
    
    # Convert mp4 to mp3
    clip = mp.AudioFileClip(mp4_path)
    mp3_path = os.path.join(save_path, sanitized_title + ".mp3")
    clip.write_audiofile(mp3_path)
    
    # Delete the original mp4 file
    os.remove(mp4_path)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Download YouTube playlist as MP3.")
    parser.add_argument("save_path", type=str, help="Path where to save the downloaded MP3 files.")
    parser.add_argument("playlist_url", type=str, help="URL of the YouTube playlist to download.")
    args = parser.parse_args()
    
    playlist = Playlist(args.playlist_url)
    
    # Constants for retries
    MAX_RETRIES = 3

    for url in playlist:
        video = YouTube(url)
        sanitized_title = sanitize_filename(video.title)

        # If video already exists, skip
        if os.path.exists(os.path.join(args.save_path, sanitized_title + ".mp3")):
            print(f"Skipping {video.title} as it has already been downloaded.")
            continue

        retries = 0
        success = False
        
        # Retry mechanism in case of download failures
        while retries < MAX_RETRIES and not success:
            try:
                download_as_mp3(video, args.save_path)
                print(f"Downloaded {video.title}")
                success = True
            except AgeRestrictedError:
                print(f"{video.title} is age restricted.")
                with open(os.path.join(args.save_path, 'ageRestricted.txt'), 'a') as f:
                    f.write(f"{url} - Age Restricted\n")
                break
            except Exception as e:
                retries += 1
                print(f"Error downloading {video.title}. Attempt {retries}/{MAX_RETRIES}. Error: {str(e)}")
                if retries == MAX_RETRIES:
                    with open(os.path.join(args.save_path, 'ageRestricted.txt'), 'a') as f:
                        f.write(f"{url} - Error: {str(e)}\n")

if __name__ == "__main__":
    main()
