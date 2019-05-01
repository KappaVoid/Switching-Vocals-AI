from constants import youtube
from videos import get_video_list_with_details_and_filter
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
def youtube_search(q, max_results, verbose=False):

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


def get_original_videos_list(switching_vocals_videos):
    for video in switching_vocals_videos:
        results  = youtube_search(video.original_video_title,25)
        high_similarity = 0
        for result in results:
            similarity = similar(video.original_video_title,result.title)
            print("Checking similarity between ", video.original_video_title, " and ", result.title," ... ", similarity)
            if similarity > high_similarity:
                high_similarity = similarity
                video.orginal_video = result

    return switching_vocals_videos



 