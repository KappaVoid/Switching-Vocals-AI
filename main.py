from search_videos import get_original_videos_list
from playlists import get_playlist_videos,get_playlist_videos_url, get_list_videos
from apiclient.errors import HttpError
from download_videos import downloadVideoList
from pytube import YouTube

import sys


def download(title, duration, youtube_url, filename, switching_vocals = False):
    if((duration > 5) or (switching_vocals == True and "switching vocals" not in title.lower())):
        return False # or too big or not switching vocal
    else:
        folder = './switching/' if switching_vocals else './original/'
        return download_music(youtube_url, folder, filename)


def download_music(youtube_url, folder, filename):
    try:
        yt = YouTube(youtube_url)
        yt.streams.filter(only_audio=True).first().download(folder, filename=filename)
        return True
    except:
        return False

def download_music_and_sv(music_list):
    
    for video in music_list:
        title, duration, yt_url = video.title, int(video.minutes), video.url
    
        if(download(title, duration, yt_url, filename=video.title, switching_vocals=True) == False):
            print("Error")
            continue # if we cant download switching music, we dont need the original
        
        title, duration, yt_url = video.title, int(video.original_video.minutes), video.original_video.url
        download(title, duration, yt_url, filename=video.original_video.title, switching_vocals=False)        


if __name__ == "__main__":
    try:

        videos_list = get_list_videos([
              get_playlist_videos("PLUfzP4gSsXLKa7kz7jxA8ckLhgAuH0uPR"),
              get_playlist_videos("PLbI4yq2djPIiprMcQON5YCFdQCv_OL6Yw")
        ])

        switching_vocals_list =  get_playlist_videos_url([
            videos_list
        ])

        orignal_song_list = get_original_videos_list(videos_list[0:2])

        download_music_and_sv(orignal_song_list)

    
        #downloadVideoList(switching_vocals_list,"./SwitchingVocalsVideos")


    except(HttpError, e):
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))


