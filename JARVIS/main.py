
from jarvis_class import jarvis
import speech_recognition as sr
import threading
import pyttsx3


if __name__=="__main__":

    s= jarvis()
    s.start_conversation_log()
    sleep = True
    while True:
        if(sleep):
            response = s.listen() 
        command = s.hear()
        sleep = s.analyze(command)               