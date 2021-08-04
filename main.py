import caption_api
import caption_processor

transcript_file_name = "CAPTION_TRANSCRIPT"
offending_words = {"apple", "orange", "grape", "strawberry"}

def main():
        #youtube = caption_api.api_setup()

        #set to whatever file name you want
        #TODO Get youtube link from user
        vid_id = "lIbjyFjiF5M"

        #retrive captions for the given video
        #vid_data = caption_api.video_search(vid_id, youtube)
        #caption_api.cap_search(vid_data, transcript_file_name, youtube)

        #read the file and search for offending words
        caption_processor.transcript_search(transcript_file_name, offending_words)


if __name__ == "__main__":
    main()