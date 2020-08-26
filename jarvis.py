import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')# print(voices) to get the object    
engine.setProperty('voice',voices[0].id)

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rganga757@gmail.com','your-password')
    server.sendmail('rganga757@gmail.com',to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir, I am Jarvis, How may I help you")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir, I am Jarvis, How may I help you")
    else:
        speak("Good evening sir, I am Jarvis, How may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"Request:{query}\n")
    except Exception as e:                                  #you can  print(e)
        speak("Cannot hear you sir, seems like the system is offline")
        return "None"
    return query


wishMe()
x=1
while x==1:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia.....')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("Wikipedia says")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        speak("Opening youtube sir")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")
    elif 'open google' in query:
        speak("Opening google sir")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
    elif 'play music' in query:
        music_dir="D:\\audioFiles\\Songs"
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strTime}")
    elif 'open code' in query:
        codePath="C:\\Users\\rgang\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'email to ravi' in query:
        try:
            speak("What is the message")
            content=takeCommand()
            to="rganga757@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("Sorry sir, could not send the email")
    elif 'sachin bhati' in query:
        speak("Sachin Bhati is the owner of AgriFlona group and an open-minded person. He is into his own world of creation and in search for creatin somethin new")
    elif 'go to sleep' in query:
        speak("Goodbye sir, Have a nice day")
        x=0