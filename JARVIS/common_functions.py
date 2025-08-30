import speech_recognition as sr
import variables as vr
import re



recognizer = sr.Recognizer()
microphone = sr.Microphone()
engine = vr.engine


def speak(text):
        engine.say(text) 
        engine.runAndWait()


# for taking command for internal program
def takeCommand(threshold=0.5):

    text = str()
    with sr.Microphone () as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = threshold 
        print("Listening...")  
        audio = recognizer.listen(source)
    try:
        # print("Recognizing..")  
        text = recognizer.recognize_google(audio,language='en-PK')
        print(f"User said :{text}\n")

    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Network error.") 

    return (text.casefold()) 


#  for printing list with numbering   
def print_list(list_name):
    i = 0
    while i < len(list_name):
        print(str(i+1)+ ": "+ list_name[i])
        i = i + 1  


# string number converter
def nsti(string,pos = None):
    l = list()
    a=re.split(r'[:,\s]\s*',string)
    for b in a:
        try:
            l.append(int(b))

        except:
            if b in vr.number_dictionary.keys() :
                l.append(vr.number_dictionary.get(b)) 

    if pos == None:            
        return l[-1]
    else:
        return l[pos]



# for removing search words 
def remove_search_word(text,extra=''):
    for words in vr.SEARCH_WORDS.keys():
        text = text.replace(words,'')
    for words in vr.EXTRA_SEARCH_WORDS:
        text = text.replace(words,'')    
    text = text.replace(extra,'')
    return text        