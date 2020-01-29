from PIL import Image, ImageTk
import pyttsx3
import pyaudio
import wikipedia
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib
import _tkinter
import tkinter

AINAME = "Friday"
logo_dir = "logo.png"

top = tkinter.Tk()
top.configure(bg='#091219')


moz_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
# engine.setProperty('rate',160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour <12:
        speak("Good Morning.....")
    elif hour >12 and hour<16:
        speak("Good Afternoon.....")
    else:
        speak("Good Evening.....")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Waiting for a command from you")
        audio = r.listen(source)

    try : 
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"Command :  {query}\n")
        return query

    except Exception as e:
        speak("Couldn't get you, can you repeat it?")
        takeCommand()

    

#main functions start
def main():
    speak("Hi.....I am " + AINAME)
    greetings()

    query = takeCommand()

    #logic for executing tasks
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak(results)

    elif 'open youtube' in query.lower():   #will open youtube
        url = "www.youtube.com"
        webbrowser.get(moz_path).open(url)

    elif 'play music' in query.lower():     #will play files in the music directory
        songs_dir = "C:/Users/John Peter/Music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        hour = datetime.datetime.now().hour
        mini = datetime.datetime.now().minute
        if hour == 12 :
            meridian = "pm"
        elif hour > 12 : 
            hour = hour -12
            meridian = "pm"
        else:
            meridian = "am"
        hour = str(hour)
        mini = str(mini)
        speak(f"The time is {hour}{mini}{meridian}")


    elif 'live stream' in query.lower():
        url = "http://192.168.43.123/index.html"
        webbrowser.get(moz_path).open(url)


 
#main()


#GUI code below
canvas = tkinter.Canvas(top, width = 160, height = 160, bg='#091219',bd=0, highlightthickness=0, relief='ridge')  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(logo_dir))  
canvas.create_image(10, 20, anchor=tkinter.NW, image=img) 

    

lbl_title = tkinter.Label(top, text = AINAME, width = 50, bg="#091219", fg="#ffffff", bd = 0, highlightthickness=0,relief='ridge')
lbl_title.config(font=("Courier", 85))
btn_Activate = tkinter.Button(top, text ="Activate", command = main, width = 25, bg="#081016", fg="#ffffff", bd = 2, highlightthickness=0)
btn_Activate.config(font=("Courier",20))

# logo.pack()
lbl_title.pack()
btn_Activate.pack() 
top.mainloop()



