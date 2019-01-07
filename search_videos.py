from apiclient.discovery import build
from constants import DEVELOPER_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION
from videos import get_video_list_with_details_and_filter


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.


def youtube_search(q, max_results, verbose=False):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=q,
        part="id",
        maxResults=max_results
    ).execute()

    search_videos_id = []
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            search_videos_id.append(search_result["id"]["videoId"])

    video_ids = ",".join(search_videos_id)

    return get_video_list_with_details_and_filter(video_ids, verbose)
