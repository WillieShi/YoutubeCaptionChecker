import transcript

def main():
        youtube = transcript.api_setup()

        #TODO Get youtube link from user
        vid_id = "lIbjyFjiF5M"

        vid_data = transcript.video_search(vid_id, youtube)
        transcript.cap_search(vid_data, youtube)


if __name__ == "__main__":
    main()