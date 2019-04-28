import re
from youtube_video import YoutubeVideo
from constants import youtube


def should_add_video(youtube_video):
    result = bool(re.search(r"mashup|medley|,|;|cover|X", youtube_video.title, flags=re.IGNORECASE)) \
             or " \\ " in youtube_video.title \
             or " / " in youtube_video.title \
             or "\\\\" in youtube_video.title \
             or " ✗ " in youtube_video.title \
             or " // " in youtube_video.title

    # print(youtube_video.title, "matches filter : ", result, "\n")
    return not result


def get_video_list_with_details_and_filter(video_ids, verbose=False):
    videos_list_response = youtube.videos().list(
        id=video_ids,
        part='snippet,contentDetails'
    ).execute()
    videos = []

    for video_result in videos_list_response.get("items", []):
        video_url = "https://www.youtube.com/watch?v=" + video_result["id"]
        youtube_video = YoutubeVideo(
            title=video_result["snippet"]["title"],
            url=video_url,
            duration=video_result["contentDetails"]["duration"]
        )
        if verbose:
            print("Video Title: ", video_result["snippet"]["title"] + "\n")
            print("Video Url :", video_url + "\n")
            print("Video duration  :", video_result["contentDetails"]["duration"] + "\n")
            print("==============================================\n")

        if should_add_video(youtube_video):
            print(youtube_video.title)
            videos.append(youtube_video)


    return videos
