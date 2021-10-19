import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
from random import randrange
import smtplib

random = randrange

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Please go and study bitch")

    else:
        speak("Good Evening!")

    speak("I am Charlie Jacket bitch I- I mean sir, How may i help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I can hear u bitch")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("I am recognizing ur crappy voice")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please say it again or i will not regret killing u")
        return "None"
    return query


stop = False


if __name__ == "__main__":
    wishMe()
    while not stop:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Assholepedia")
            print(results)
            speak(results)

        if 'quit' in query:
            speak(
                "Ok i am going Please call me again if you want someone to eat your brain!! bye")
            print(
                'Ok i am going Please call me again if you want someone to eat your brain!! bye')
            stop = True

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
            speak("Ok i have opened youtube")

        elif 'open wikipedia' in query:
            webbrowser.open('https://www.wikipedia.org/')
            speak(
                'Ok i have opened wikipedia, But you could have also asked me (the name of the thing + wikipedia')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
            speak('Ok i have opened google')

        elif 'open stackoverflow' in query:
            webbrowser.open('http://stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Downloads\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            code = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)

        if 'hai' in query:
            speak(f"Hello")

        if 'hello' in query:
            speak(f"Hi")

        if 'hay' in query:
            speak('hey')

        if 'wassup' in query:
            speak("I am fine what about you?")

        if 'who ordered you' in query:
            speak("I was coded by Jayraj Sinvhal")

        if 'Fuck you' in query:
            speak("Oh you too")

        elif 'will you marry' in query:
            speak("Nope i friend zone you")

        if 'in which language were you coded' in query:
            speak("I was coded in a programming language named Python")
        elif 'pic' in query:
            speak(f"{query}")
