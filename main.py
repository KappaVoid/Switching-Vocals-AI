
from search_videos import youtube_search
from oauth2client.tools import argparser

if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--max-results", help="Max results", default=25)
    args = argparser.parse_args()

    try:
        youtube_search(args)
    except(HttpError, e):
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))