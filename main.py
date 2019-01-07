from search_videos import youtube_search
from playlists import get_playlist_videos
from apiclient.errors import HttpError
import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            print(len(get_playlist_videos("PLUfzP4gSsXLKa7kz7jxA8ckLhgAuH0uPR")))
            print(len(get_playlist_videos("PLbI4yq2djPIiprMcQON5YCFdQCv_OL6Yw")))
            #youtube_search(q=sys.argv[1],max_results=sys.argv[2])
    except(HttpError, e):
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
