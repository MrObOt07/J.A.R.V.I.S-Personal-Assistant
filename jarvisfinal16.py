import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser # inbulit in python
import psutil
import pyjokes
import os
import pyautogui # pip install pyautogui


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I;%M:%S") #for 12 hour clock
    speak("The curent time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Wellcome Back yugan")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    elif hour>=18 and hour<24:
        speak("Good Evening ")
    else:
        speak("Good Night . Sweet Drems!")

    speak("Jarvis at your service . Please tell me how can i help your")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/ADMIN/Desktop/screenshot.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)
    
def jokes():
    speak(pyjokes.get_joke())
    

if __name__ == "__main__":
    wishme() 

    while True:
        query = takecommand().lower()

        #All commands will be stored in lower case in query
        #for easy recognition

        if 'time' in query: # tell us time when asked
            time_()
        
        elif 'date' in query: # tell us date when asked
            date_()
        
        elif 'play music' in query:
            musicdir="Music"
            songs=os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[30]))

        elif 'open vs code' in query:
            codepath="C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath1="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath1)
        
        elif "wikipedia" in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open chrome' in query:
            speak('What shold i serach?')
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe "
            os.startfile(codepath)

        elif 'search chrome' in query:
            speak('What shold i serach?')
            search_Team = takecommand().lower()
            speak("Searching....")
            webbrowser.open('https://www.google.com/search?q='+search_Team)
       

        elif 'search youtube' in query:
            speak('What shold i serach?')
            search_Team = takecommand().lower()
            speak("Hera We go to YOU TUBE!!!")
            webbrowser.open('https://www.youtube.com/results?search_query='+search_Team)
        
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()

        elif 'go offline' in query:
            speak('Going Offline Sir!!')
            quit()

        elif 'write a note' in query:
            speak("What should i write sir?")
            notes = takecommand()
            file = open('notes.txt', 'w')
            speak("Sir should i include Date and Time?")
            ans = takecommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%I:%M")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, sir!')
            else:
                file.write(notes)
                
        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())
        
        elif 'screenshot' in query:
            screenshot()
        
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            webbrowser.open_new_tab("https://www.google.com/maps/place"+location)

        elif 'log out' in query:
            os.system("shutdown -l")     

        elif 'restart' in query:
            os.system("shutdown /r /t 1")       

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1 ")       
              
            
                   
