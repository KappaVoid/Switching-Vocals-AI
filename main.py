from search_videos import youtube_search
from playlists import get_playlist_videos,get_playlist_videos_url
from apiclient.errors import HttpError
from download_videos import downloadVideoList

import sys

if __name__ == "__main__":
    try:
        switching_vocals_list =  get_playlist_videos_url([
              get_playlist_videos("PLUfzP4gSsXLKa7kz7jxA8ckLhgAuH0uPR"),
              get_playlist_videos("PLbI4yq2djPIiprMcQON5YCFdQCv_OL6Yw")
        ])

        downloadVideoList(switching_vocals_list,"./SwitchingVocalsVideos")

    except(HttpError, e):
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
