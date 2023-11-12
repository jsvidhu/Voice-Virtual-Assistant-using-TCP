import socket
import pyttsx3
import webbrowser 
import speech_recognition as sr
import time
from tkinter import*
import sys

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
statement=""
str1="search"

def speak(text):
    engine.say(text)
    engine.runAndWait()

class Widget:
    def __init__(self):
        self.root = Tk()
        self.root.title('Nova Virtual Assistant')
        self.root.geometry('540x350')

        #ScrollBar
        scrollbar=Scrollbar(self.root)
        scrollbar.pack(side=RIGHT,fill=Y)

        self.userText = StringVar()
        self.userText.set('Nova Your Virtual Assistant')
        
        self.top = Message(textvariable=self.userText, bg='black',fg='white')
        self.top.config(font=("Century Gothic", 15, 'bold'))
        self.top.pack(side='left', fill='both', expand='yes')

        #Text box
        self.my_text=Text(self.root , width=40 , height=5)
        self.my_text.pack(fill='both', expand='yes')

        self.btn = Button(self.root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        self.btn2 = Button(self.root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=self.close).pack(fill='x', expand='no')
        speak("Hi I am Nova you virtual assistant. how can i help you ?")
        self.root.mainloop()
                

    #CLOSE FUNCTION
    def close(self):
        client_socket.send(bytes("exit",'utf-8'))
        time.sleep(2)
        client_socket.close()
        sys.exit()
        
    #CLICK FUNCTION
    def clicked(self):
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                
                try:
                    statement=r.recognize_google(audio,language='en-in')
                    self.my_text.insert(INSERT,"USER:")
                    self.my_text.insert(INSERT,statement)
                    
                    client_socket.send(bytes(statement,'utf-8'))
                    
                    #receving from server
                    s=client_socket.recv(1024)
                    self.my_text.insert(INSERT,"\nNOVA:")
                    self.my_text.insert(INSERT,s.decode('utf-8'))
                    self.my_text.insert(INSERT,"\n")


                except sr.UnknownValueError:
                    self.my_text.insert(INSERT,"\nNOVA:")
                    self.my_text.insert(INSERT,"Sorry ,I could not understand what you said\n")
                    
                    speak("Sorry ,I could not understand what you said")
            
if __name__== '__main__':
    widget = Widget()

