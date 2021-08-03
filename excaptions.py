# -*- coding: utf-8 -*-

# Sample Python code for youtube.captions.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery

# Call the API's captions.download method to download an existing caption track.
def download_caption(youtube, caption_id, tfmt):
    subtitle = youtube.captions().download(
    id=caption_id,
    tfmt=tfmt
    ).execute()
    print("First line of caption track: %s" % (subtitle))
# Call the API's captions.list method to list the existing caption tracks.
def list_captions(youtube, video_id):
    results = youtube.captions().list(
    part="snippet",
    videoId=video_id
    ).execute()

    for item in results["items"]:
        id = item["id"]
        name = item["snippet"]["name"]
        language = item["snippet"]["language"]
        print ("Caption track '%s(%s)' in '%s' language." % (name, id, language))

    return results["items"]
def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyANDDH0HwD_q4A2O2wu4qb5jldIHacW3O0"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    # request = youtube.captions().list(
    #     part="snippet",
    #     videoId="M7FIvfx5J10"
    # )
    # response = request.execute()

    # print(response)
    list_captions(youtube, 'M7FIvfx5J10')
    download_caption(youtube, '8yMV7mc691aTqjNxZ9zPHOdwpkL_e11j', 'srt')

if __name__ == "__main__":
    main()


