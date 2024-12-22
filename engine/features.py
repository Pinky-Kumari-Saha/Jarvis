from playsound import playsound
import eel
import os
import re
from engine.config import ASSISTANT_NAME
from engine.command import speak
# from engine.command import extract_yt_term
import pywhatkit as kit



#playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\strange-notification-36458.mp3"
    playsound(music_dir)
    
 #open function
def openCommand(query):
     query=query.replace(ASSISTANT_NAME,"")
     query=query.replace("open","")
     query.lower()
     
     if query !="":
        speak("Opening" + query)
        os.system('start' + query) 
        
        
     else:
        speak("not found")  
        
        
#add youtube
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing" +search_term+ "on YouTube")
    kit.playonyt(search_term)
    
    
     
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None                  