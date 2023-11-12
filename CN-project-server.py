import socket
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pywhatkit
import datetime
import time


server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(5)
client_socket,addr=server_socket.accept()

#Voice Declaration   
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
statement=""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        statement=r.recognize_google(audio,language='en-in')
        return statement

while True:
    data=client_socket.recv(1024)
    query= data.decode('utf-8')
    
    if "open google" in query.lower():
        speak("Opening Google ")
        client_socket.send(bytes("Opening google....",'utf-8'))
        time.sleep(1)
        webbrowser.open("https://google.com/")
        
    elif "play" in query.lower():
        song = query.lower().replace('play', '')
        speak('playing ' + song)
        client_socket.send(bytes('Playing ' + song,'utf-8'))
        pywhatkit.playonyt(song)
        
    elif "who are you" in query.lower():
        speak("Hi I am Nova you virtual assistant")
        client_socket.send(bytes("Hi I am Nova you virtual assistant",'utf-8'))

    elif "what is the time" in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        client_socket.send(bytes(f"the time is {strTime}",'utf-8'))
        time.sleep(1)
        speak(f"the time is {strTime}")
        
    elif "open gmail" in query.lower():
        client_socket.send(bytes("Opening gmail....",'utf-8'))
        time.sleep(1)
        speak("Opening Gmail")
        webbrowser.open("https://gmail.com/")
        
    elif "open youtube" in query.lower():
        client_socket.send(bytes("Opening Youtube....",'utf-8'))
        time.sleep(1)
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com/")        

    elif "search" in query.lower():
        client_socket.send(bytes("What do you want to search ?",'utf-8'))
        time.sleep(1)
        speak("What do you want to search ?")
        s=takeCommand()
        url='http://google.com/search?q=' + s
        webbrowser.get().open(url)
        time.sleep(1)
        speak("Here is what I found .")
        
    elif "music" in query.lower():
        client_socket.send(bytes("Opening Music player....",'utf-8'))
        time.sleep(2)
        speak("Opening Music Player")
        os.startfile(os.path.join("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Windows Media Player.lnk"))
        
    elif "exit" in query.lower():
        speak("Bye Have a good day.")
        time.sleep(2)
        break
        
    else:
        speak("Sorry ,I don't think I can do that")
        client_socket.send(bytes("Sorry ,I don't think I can do that.",'utf-8'))
        
    
