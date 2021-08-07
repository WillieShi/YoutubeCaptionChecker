import caption_api
import caption_processor
import urlparser
import word_list_builder

transcript_file_name = "CAPTION_TRANSCRIPT"
word_list = {}

def main():
        #get video link from user and parse vid id
        input1 = str(input("Enter your youtube link:"))
        vid_id = urlparser.parse_vid_id(input1)
        
        #build wordlist
        word_list = word_list_builder.list_build()
        
        #set up api query
        youtube = caption_api.api_setup()

        #retrive captions for the given video
        vid_data = caption_api.video_search(vid_id, youtube)
        caption_api.cap_search(vid_data, transcript_file_name, youtube)

        #read the file and search for offending words
        caption_processor.transcript_search(transcript_file_name, word_list)


if __name__ == "__main__":
    main()