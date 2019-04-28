from apiclient.discovery import build
DEVELOPER_KEY = "AIzaSyBqAlpo4qiJgkgmM3Pj_IM80gFDecOFghA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
