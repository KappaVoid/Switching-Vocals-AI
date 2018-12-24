
from search_videos import youtube_search
from apiclient.errors import HttpError
import sys


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            youtube_search(q=sys.argv[1],max_results=sys.argv[2])
    except(HttpError, e):
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))