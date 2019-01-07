from constants import DEVELOPER_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION
from videos import get_video_list_with_details_and_filter
from apiclient.discovery import build


def get_playlist_videos(playlist_id, verbose=False):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    playlistitems_list_request = youtube.playlistItems().list(
        playlistId=playlist_id,
        part="snippet",
        maxResults=50
    )

    videos = []
    playlist_videos = []
    while playlistitems_list_request:
        playlistitems_list_response = playlistitems_list_request.execute()

        # Print information about each video.
        for playlist_item in playlistitems_list_response["items"]:
            title = playlist_item["snippet"]["title"]
            video_id = playlist_item["snippet"]["resourceId"]["videoId"]
            if verbose:
                print("%s (%s)" % (title, video_id))
            videos.append(video_id)

        playlist_videos.extend(get_video_list_with_details_and_filter(",".join(videos), verbose))
        videos.clear()
        playlistitems_list_request = youtube.playlistItems().list_next(
            playlistitems_list_request, playlistitems_list_response)

    return playlist_videos
