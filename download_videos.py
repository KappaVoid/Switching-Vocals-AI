from __future__ import unicode_literals
from  youtube_dl import YoutubeDL as VideoDownloader  


def downloadVideoList(video_url_list,dir_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': dir_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    with VideoDownloader(ydl_opts) as ydl:
        ydl.download(video_url_list)





 