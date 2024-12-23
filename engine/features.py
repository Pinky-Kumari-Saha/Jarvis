import struct
import time
from playsound import playsound
import eel
import os
import re
import webbrowser
import sqlite3
import pvporcupine
import pyaudio # type: ignore
from engine.config import ASSISTANT_NAME 
from engine.command import speak
# from engine.command import extract_yt_term
import pywhatkit as kit
# from engine.helper import extract_yt_term
import pyautogui as autogui



con = sqlite3.connect("jarvis.db")
cursor = con.cursor()



#playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\strange-notification-36458.mp3"
    playsound(music_dir)
@eel.expose    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()  # Convert query to lowercase

    app_name = query.strip()  # Clean up any extra spaces
        
    if app_name != "":  # Check if the app name is not empty
        try:
            # Query the database for the path of the application
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()
                
            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])  # Open the application
                    
            elif len(results) == 0:
                # Query the database for a URL associated with the command
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                    
                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])  # Open the URL
                else:
                    # If no app or URL is found, try opening it as a command
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)  # Try to run the command
                    except Exception as ex:
                        speak("Not found. Error: " + str(ex))
        except Exception as e:
            speak(f"Something went wrong: {e}")  # Handle any other errors
        
  
               
#add youtube
# @eel.expose
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing" +search_term+ "on YouTube")
    kit.playonyt(search_term)
    
    
     
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None


# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(
#             rate=porcupine.sample_rate,
#             channels=1,
#             format=pyaudio.paInt16,
#             input=True,
#             frames_per_buffer=porcupine.frame_length
#             )
#         # print("Listening for hotwords...")  
        
#         while True:
#             keyword =audio_stream.read(porcupine.frame_length)
#             keyword =struct.unpack_from("h"*porcupine.frame_length,keyword) 
            
#             keyword_index=porcupine.process(keyword) 
            
#             if keyword_index >= 0:
#                 print("hotword detected !!") 
                
#                 # import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(0.5)
#                 autogui.keyUp("win")
                
#     except :
#         # print(f"Error:{e}")
        
#     # finally :   
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate() 
# hotword()               

# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
#         paud=pyaudio.pyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)  
        
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword) 
            
#             keyword_index=porcupine.process(keyword) 
            
#             if keyword_index>=0:
#                 print("hotword detected") 
                
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()    
            
                                         