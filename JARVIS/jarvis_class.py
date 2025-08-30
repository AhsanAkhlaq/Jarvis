
import speech_recognition as sr
from datetime import date,datetime
import webbrowser
import os
import wikipedia
import smtplib
import variables as vr
from websites_opener_in_chrome import Web_opening
from movie_player import MoviePlayer
from sys import exit
import rotatescreen
import time
from common_functions import *
import threading




class jarvis:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
     #   t1 = threading.Thread(target=(self.recognizer.recognize_google(audio,language='en-IN')).casefold() , args=(10,))


    # used to listen for the wake word
    def listen(self):
        self.recognizer.dynamic_energy_threshold = 3000
        self.recognizer.pause_threshold = 0.5
        print("listening.")
        with self.microphone as source:
            while True:
                try:      
                        self.recognizer.adjust_for_ambient_noise(source)          
                        # time out 
                        audio = self.recognizer.listen(source)
                        response = (self.recognizer.recognize_google(audio,language='en-IN')).casefold() 
                        if (("exit" in response) or ("close" in response)):
                            speak("Exiting  the program.")
                            exit()   
                        elif vr.WAKE in response:
                            self.wishMe()
                            speak("How can i help you")
                            return response.casefold()            
                        else: 
                            pass
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    print("Network error.")
                     


    # Used to here the Commands after the wake word has said
    def hear(self):
  
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                # recognizer.dynamic_energy_threshold = 3000
                self.recognizer.pause_threshold = 0.5
                # time out 
                print("Waiting for command..")
                audio = self.recognizer.listen(source,timeout=5.0)
                command = str(self.recognizer.recognize_google(audio,language='en-IN')).casefold()
                self.remember(command)
                print(command)
                return command.casefold()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")
 

    # Used to track the date of the conversation ,may need to add the time in future
    def start_conversation_log(self):
        today = str(date.today())
        today = today
        with open(vr.CONVERSATION_LOG,"a") as f:
            f.write("Conversation started on: "+ today +"\n")
    

    # writes each command from user to the conversation log
    def remember(self, command):
        with open(vr.CONVERSATION_LOG,"a") as f:
            f.write("User: "+ command + "\n")
    

    # Check the first word in the commmand to determine if it's  a search word
    def find_search_words(self, command):
        if vr.SEARCH_WORDS.get(str(command).split(' ')[0]) == str(command).split(' ')[0]:
            return True


    # Intro of jarvis
    def intro(self):
        speak("Asalamu Alikum Sir! I am Jarvis Sir  Your personal asistance How can i help you or what can i do for you")


    # wish good moring etc
    def wishMe(self):
        hour = int(datetime.now().hour)
        if hour>= 0 and hour < 12:
            speak("Good Morining!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")
        self.intro()


    # for sending E-mail
    def sendEmail(self,to ,content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('muhammad.ahsan.akhlaq@gmail.com','key-----')
        server.sendmail('muhammad.ahsan.akhlaq@gmail.com',to,content)
        server.close
    





    def analyze(self, query):
        try:
            analyze_bool = False
            #   opening website in broswer
            web_open = Web_opening(query)
            analyze_bool = web_open.open()

            if (analyze_bool):


                # searching in wikipedia
                if 'wikipedia' in query:
                    speak('searching Wikipedia')
                    query = remove_search_word(query,'wikipedia')
                    results = wikipedia.summary(query,sentences=2)
                    print(results)
                    speak("According to wikipedia")
                    speak(results)
    
                # time
                elif (('time' in query) and (('what is'in query)or("what's" in query))):
                    hour = int(datetime.now().strftime("%I"))
                    minutes = int(datetime.now().strftime("%M"))
                    am_pm = datetime.now().strftime("%p")
                    speak(f"Sir, it's {hour},{minutes} {am_pm}")

                # for Google search
                elif self.find_search_words(query):
                    speak("Here is what I found.")
                    webbrowser.open("https://www.google.com/search?q={}".format(query))


                # Alarm
                elif ('alarm' in query):
                    f = open("G:\\PYTHON\\Python Programs\\JARVIS\\data.txt",'a')
                    f.write(query)
                    f.close()
                    
                    os.startfile("G:\\PYTHON\\Python Programs\\JARVIS\\Alarm.py")

                #  opening apps 
                elif (('open' in query) and ('code' in query)):
                    speak("opening Visual code.")
                    os.startfile("G:\\PYTHON\\SOFTWARE FOR PYTHON\\Microsoft VS Code\\Code.exe")
                
                # for sending Email
                elif 'send email' in query:
                    try:
                        speak("What's the message")
                        content = takeCommand(1)
                        to ="muhammad.ahsan.akhlaq.2@gmail.com"
                        self.sendEmail(to,content)
                        speak("Email has been sent")
                    except Exception as e:
                        print(e)
                        speak("Sorry sir.I am not able to send this Email")    

                # playing movies
                elif (('play' in query) or ('movie' in query) or ('movies'in query)) :
                    if (('music' in query) and ('spotify'in query)):
                        os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Spotify\\Spotify.exe")

                    MoviePlayer(query)

            
                elif('update' in query):
                    speak("Updating Myself")
                    os.popen('''pyinstaller --noconfirm --onefile --windowed  "G:/PYTHON/Python Programs/JARVIS/main.py"''')
                    return True

                elif((("hack"in query) or ("rotate" in query)) and ("screen" in query)):
                    speak("How many times do you want to rotate")
                    text = takeCommand()
                    try:
                        num = nsti(text)
                    except:
                        num = 4   
                    if num > 50:
                        speak("Tell password")
                        pas = takeCommand()
                        if pas =="ahsan":
                            pass
                        else:
                            num = 0
                    screen = rotatescreen.get_primary_display()
                    start = screen.current_orientation
                    
                    for i in range (1,(num+1)):
                        a = abs((start -i*90)% 360)
                        screen.rotate_to(a)
                        time.sleep(1)
                        
                elif (("exit" in query) or ("close" in query)):
                    speak("Exiting  the program.")
                    exit()
                
                elif ('sleep' in query):
                    speak("going to sleep.")
                    return True
                
                
                else:
                    speak("I dono't know how to do that yet.")       
        
        except TypeError:
            pass
        return False

