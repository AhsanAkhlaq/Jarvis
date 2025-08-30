
import webbrowser
import pywhatkit
from common_functions import speak,remove_search_word

class Web_opening:
    def __init__(self,query) -> None:
        self.query = query
    def open(self):
        if ((('find' in self.query) or ('search' in self.query)) and ('youtube' in self.query)):
            speak("Opening Youtube and finding search")
            search_y = remove_search_word(self.query,'youtube')
            webbrowser.open_new(f"https://www.youtube.com/results?search_query={search_y}")
            pywhatkit.playonyt(search_y)
            speak("This may helps you Sir.")

        elif (('open' in self.query) and ('youtube' in self.query)):
            speak("opening Youtube.")
            webbrowser.open_new("https://www.youtube.com/")
        elif (('open' in self.query) and (('google' in self.query) or ('chrome' in self.query))):
            speak("opening google.")
            webbrowser.open_new("https://")
        elif (('open' in self.query) and ('whatsapp' in self.query)):
            speak("opening Whatsapp.")
            webbrowser.open_new("https://web.whatsapp.com/")
        else:
            return True 
