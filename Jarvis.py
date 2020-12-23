import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
# pip install pipwin then pipwin install pyaudio otherwise speech_recognition or take
# takeCommand function will not work


engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

voice = engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good Morning")

    elif hour >=12 and hour <16:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I an Jarvis Sir, please tell me how may I assist you today?")

def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    with open("Pass_secure1.txt", "r") as f:
        password = f.read()
    server.login("s1911nitin@gmail.com", password)
    server.sendmail("s1911nitin@gmail.com", to, content)
    server.close()

def takeCommand():
    """It takes microphone input from user and returns the string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return("None")

    return(query)


if __name__ == '__main__':
    wishme()
    while(True):
        query = takeCommand().lower()
        # speak(query)

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open amazon" in query:
            webbrowser.open("amazon.com")

        elif "open flipkart" in query:
            webbrowser.open("flipkart.com")


        elif "the time" in query:
            strfttime = datetime.datetime.now().strftime("%H%M%S")
            speak(f"Sir the precious time is {strfttime}")

        elif "play music" in query:
            music_dir = "C:\\Users\\Nitin Manali\\Downloads\\My_music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "open code" in query:
            codePath = "C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
            os.startfile(codePath)

        elif "email to nitin" in query:
            try:
                speak("What would you like to forward Sir?")
                content = takeCommand()
                to = "s19nitin@gmail.com"
                sendemail(to, content)
                speak("An email has been successfully sent Sir")

            except Exception as e:
                # print(e)
                speak("I am sorry Sir as I am unable to forward an email right now due to some technical error")

        elif "quit" in query:
            speak("Good bye & have a good day Sir")
            quit()



