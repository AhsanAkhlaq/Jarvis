import pyttsx3


# Python Text-to-Speech (pyttsx3) constants
engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.0)


#  Wake word in Listen Function
WAKE = "wake"


# Usedto store user commands for analysis
CONVERSATION_LOG = "Conversation Log.txt"


# Initial anaalysis of words that would typically require a Google search
SEARCH_WORDS = {"who":"who","what":"what","when":"when","where":"where","why":"why","how":"how"}

EXTRA_SEARCH_WORDS ={'find','search','is','on','in','jarvis','do you','mean','meant'}


# dictionary for number
number_dictionary = {"one":1, "first":1, "two":2, "second":2, "three":3, "third":3, "four":4, "fourth":4, "five":5, "fifth":5, "six":6, "sixth":6, "seven":7, "seventh":7, "eight":8, "eighth":8, "nine":9, "ninth":9, "ten":10, "tenth":10 }


# movie data excel file path
movie_file_path = "G:\\PYTHON\\Python Programs\\JARVIS\\movie_list.xlsx"