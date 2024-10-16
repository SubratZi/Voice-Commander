import speech_recognition as sr
import pyttsx3 
import sys
import webbrowser
import json

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def command(voice):
    data = json.load(open('data.json'))
    webbrowser.open(data[voice.lower()])
    initialvoice = (voice.lower().split(" "))
    initialvoice.remove('open')
    initialvoice.remove('please')
    finalvoice = initialvoice
    speak(f"Opening {finalvoice}")

if __name__ == "__main__":
    speak("Initializing Jarvis")

r = sr.Recognizer()
print("Listening....")
looptime = 0
while looptime <= 3:
    looptime += 1
    try:
        with sr.Microphone() as source:
            audio = r.listen(source, timeout=2,phrase_time_limit=2)
            speech = r.recognize_google(audio)
        if speech.lower() == "jarvis":
            speak("Yes sir What do you want me to do?")
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=3,phrase_time_limit=4)
                speech = r.recognize_google(audio)
                if speech.lower()!= "close":
                    print(speech.lower())
                    if "please" in speech.lower():
                        command(speech)
                        break
            sys.exit(0)
        elif speech.lower() == "close":
            sys.exit(0)

    except sr.UnknownValueError:
        print("Audio is not audible or wakeupcall not given, Try Again")
    except sr.RequestError:
        print("Error in Requesting")
    