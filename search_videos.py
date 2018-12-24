

from apiclient.discovery import build
from youtbe_video import YoutubeVideo


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBqAlpo4qiJgkgmM3Pj_IM80gFDecOFghA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results, verbose = False):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=q,
        part="id",
        maxResults=max_results
    ).execute()

    videos = []
    search_videos_id = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            search_videos_id.append(search_result["id"]["videoId"])

    video_ids = ",".join(search_videos_id)

    # Call the API's videos.list method to retrieve the video resource.
    videos_list_response = youtube.videos().list(
        id=video_ids,
        part='snippet,contentDetails'
    ).execute()

    for video_result in videos_list_response.get("items", []):
        video_url =  "https://www.youtube.com/watch?v=" + video_result["id"]
        if(verbose == True):
            print("Video Title: ", video_result["snippet"]["title"] + "\n")
            print("Video Url :", video_url + "\n")
            print("Video duration  :", video_result["contentDetails"]["duration"] +"\n")
            print("==============================================\n")
        videos.append(
            YoutubeVideo(
                title=video_result["snippet"]["title"],
                url=video_url,
                duration=video_result["contentDetails"]["duration"]
            )
        )
    return videos


