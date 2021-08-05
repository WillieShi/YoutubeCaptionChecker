import caption_api
import caption_processor
import urlparser

transcript_file_name = "CAPTION_TRANSCRIPT"
offending_words = {"apple", "orange", "grape", "strawberry"}

def main():
        #get video link from user and parse vid id
        input1 = str(input("Enter your youtube link:"))
        vid_id = urlparser.parse_vid_id(input1)
        
        #set up api query
        youtube = caption_api.api_setup()
        
        #set to whatever file name you want

        #retrive captions for the given video
        vid_data = caption_api.video_search(vid_id, youtube)
        caption_api.cap_search(vid_data, transcript_file_name, youtube)

        #read the file and search for offending words
        caption_processor.transcript_search(transcript_file_name, offending_words)


if __name__ == "__main__":
    main()