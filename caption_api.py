import io
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaIoBaseDownload

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def api_setup():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    return youtube
#pulls up video data for a given videoID
def video_search(vid_id, youtube):
    vid_data = youtube.captions().list(
        part="snippet",
        videoId = vid_id
    ).execute()
    return vid_data

#The current cap_search only looks for the asr or auto generated captions for a given video
def cap_search(vid_data, transcript_file_name, youtube):
    #grab the auto generated caption track from the given video
    caption_id = ""
    for item in vid_data["items"]:
        if item["snippet"]["trackKind"] == "asr":
                caption_id = item["id"]

    if caption_id == "":
        print("Caption ID for video not found")
        exit()
    request = youtube.captions().download(
        id = caption_id
    )

     # TODO: For this request to work, you must replace "YOUR_FILE"
    #       with the location where the downloaded content should be written.
    fh = io.FileIO(transcript_file_name, "wb")

    download = MediaIoBaseDownload(fh, request)
    complete = False
    while not complete:
      status, complete = download.next_chunk()
