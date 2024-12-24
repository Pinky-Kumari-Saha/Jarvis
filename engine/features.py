from shlex import quote
import struct
import subprocess
import time
from playsound import playsound
import eel
import os
import re
 
import pyautogui as autogui
import webbrowser
import sqlite3
import pvporcupine
import pyaudio # type: ignore
from engine.config import ASSISTANT_NAME 
from engine.command import speak

import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words
# from .helper import extract_yt_term  # Relative import





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
    
    
     
# def extract_yt_term(command):
#     pattern = r'play\s+(.*?)\s+on\s+youtube'
#     match = re.search(pattern,command,re.IGNORECASE)
#     return match.group(1) if match else None

    
# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
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
import time
import struct
import pyaudio
import pvporcupine
import pyautogui as autogui

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Initialize Porcupine for keyword detection with a list of keywords
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        paud = pyaudio.PyAudio()

        # Open audio stream from the microphone
        audio_stream = paud.open(rate=porcupine.sample_rate,
                                  channels=1,
                                  format=pyaudio.paInt16,
                                  input=True,
                                  frames_per_buffer=porcupine.frame_length)

        print("Listening for hotwords...")

        # Main loop for audio streaming
        while True:
            # Read audio data from the microphone
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # Process audio data to detect keywords
            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print("Hotword detected")

                # Press shortcut key Win + J using pyautogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up resources on exit
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

        print("Hotword detection stopped.")
        
# find contacts
def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
    
# whatsApp function
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12        
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7         
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6          
        message = ''
        jarvis_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    autogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        autogui.hotkey('tab')

    autogui.hotkey('enter')
    speak(jarvis_message)
    
        

