import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search
from lib.google_search_results import GoogleSearchResults
import sys
from threading import Thread
import time
import winsound



new=2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  



speak("Hi, I'm Lana your personal assistant. Speed 1 terahertz, memory 1 zigabyte.")
print("Hi, I'm Lana your personal assistant. Speed 1 terahertz, memory 1 zigabyte.")

  

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        frequency = 1400  # Set Frequency To 2500 Hertz
        duration = 300  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    speak("How may I help you today?")
    print("How may I help you today?")
    while True:
    # if 1:
        query = takeCommand().lower()

 # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
           pass

        elif 'goodbye' in query:
           speak("Goodbye Sir")
           break
        
        elif 'bye' in query:
            speak("Goodbye Sir")
            break
        
        elif 'search'or 'open' and 'google'in query:
   
            query = query.replace("search", "")
            query = query.replace("google", "")
            webbrowser.open("http://www.google.com/?#q="+query,new=new)
        
        
        
        elif 'search' or'open' and 'youtube'in query:
       
            query = query.replace("search", "")
            query = query.replace("youtube", "")

            webbrowser.open("http://www.youtube.com/results?search_query="+query,new=new)


                



