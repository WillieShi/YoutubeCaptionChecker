import io
import os

from pyasn1.type.univ import Null

def transcript_search(transcript_file_name, offending_words):
        file = open(transcript_file_name, 'r')

        #caption file is structured like l1: time_stamp, l2: text, l3: empty \n
        #go through file and search for offending_words
        line = file.readline()
        while line:
                if line != '\n':
                        timestamp = line
                        text = file.readline()
                        word = word_check(text, offending_words)
                        if word != "":
                                print("time: " + timestamp + "line: " + text + "word: " + word + "\n")
                line = file.readline()
        file.close()
                        
def word_check(line, offending_words):
        words = line.split()
        
        for word in words:
                if word in offending_words:
                        return word
        return ""


                        