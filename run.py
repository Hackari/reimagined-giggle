import subprocess
from datetime import datetime

def yyyymmdd():
    curr = datetime.now()
    curr = curr.strftime("%Y%m%d")
    return curr

def conv(input_file, curr):
    with open(input_file, 'r') as file:
        links = file.read().splitlines()
    yt_dlp_exe_path = "./yt-dlp.exe"
    for link in links:
        command = [
            yt_dlp_exe_path,
            "--extract-audio",
            "--audio-format", "mp3",
            "-o", f".\{curr}\%(title)s.%(ext)s",
            link
        ]
        try:
            subprocess.run(command, check=True)
        except:
	    continue

if __name__ == "__main__":
    conv("youtube_links.txt", yyyymmdd())
 