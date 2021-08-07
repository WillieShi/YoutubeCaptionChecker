import io
import os

words_file_name = "WORDS.txt"

#populates word_list set based off words file
def list_build():
        file = open(words_file_name, 'r')

        word_list = set()
        Lines = file.readlines()
        for line in Lines:
                word_list.add(line.strip())
        file.close()
        return word_list

#adds words or phrases to the designated words file
def list_add(new_word):
        file = open(words_file_name, 'a')
        file.write("\n")
        file.write(new_word)
        file.close()
def list_remove(word):
        file = open(words_file_name, "r")

        lines = file.readlines()
        file.close()

        new_file = open(words_file_name, "w")
        for line in lines:
                if line.strip("\n") != word:
                        new_file.write(line)

        new_file.close()
def list_clear():
        file = open(words_file_name, "w")
        file.truncate()
        file.close()

