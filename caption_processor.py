import io
import os

def transcript_search(transcript_file_name, offending_words):
        file = open(transcript_file_name, 'r')

        #caption file is structured like l1: time_stamp, l2: text, l3: empty \n
        #go through file and search for offending_words
        line = file.readline()
        print(line)
        while line:
                if line != '\n':
                        timestamp = line
                        text = file.readline()
                        if word_check(text, offending_words):
                                print("time: " + timestamp + "line: " + text + "\n")
                line = file.readline()
                        
def word_check(line, offending_words):
        words = line.split()
        
        for word in words:
                if word in offending_words:
                        return True
        return False


                        