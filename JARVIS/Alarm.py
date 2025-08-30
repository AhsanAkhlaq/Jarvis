from datetime import datetime
from playsound import playsound
import variables as vr
import re




extracted_time = open('G:\\PYTHON\\Python Programs\\JARVIS\\data.txt','rt')
tiime_string= str(extracted_time.read())


delete_time = open("G:\\PYTHON\\Python Programs\\JARVIS\\data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

engine = vr.engine
def speak(text):
    engine.say(text) 
    engine.runAndWait()

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


def alarm(text):
    hour = minutes = None
    try:
        hour = nsti(text,0)
        try:        
            minutes = nsti(text,1)
        except IndexError:
            minutes = 0
    except IndexError:
        print ('no time is given')


            
    print (hour ,minutes)
    loop = True

    speak(f"Alarm set fo {hour} {minutes}")
    if hour > 12:
        pass
    if hour == 12:
        pass
    elif (('pm' in text) or ('p.m' in text) or ('p.m.' in text)):
        hour = hour + 12 
  
        
    while loop:
        chour = int(datetime.now().strftime('%H'))   
        if hour == chour:
            while True:
                cminutes = int(datetime.now().strftime("%M"))
                if minutes == cminutes:
                    print("Wake Up Sir , It's Time To Work .")
                    playsound("G:\\PYTHON\\Python Programs\\JARVIS\\Sounds\\1.mp3")     
                elif minutes < cminutes:
                    loop = False
                    break
        elif hour < chour:
            break


alarm(tiime_string)        