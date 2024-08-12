import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from gtts import gTTS
import pygame
import os
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('hello.mp3')
# import time

# Initialize Pygame mixer
    pygame.mixer.init()

# Load MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play MP3 file
    pygame.mixer.music.play()

# Keep the script running while the music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Check if the music is still playing
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
    elif "open stackoverflow" in c.lower():
        webbrowser.open("https://www.stackoverflow.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open medium" in c.lower():
        webbrowser.open("https://www.medium.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://www.gmail.com")
    elif "open drive" in c.lower():
        webbrowser.open("https://www.drive.google.com")
    elif "open classroom" in c.lower():
        webbrowser.open("https://www.classroom.google.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        pass
if __name__ == '__main__':
    speak("Initializing...")
    while True:
        r = sr.Recognizer()      
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Yup, I'm here")
                # listen for command
                with sr.Microphone() as source:
                    print("jarvis is active")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
        
