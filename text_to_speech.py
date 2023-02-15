import pyttsx3

engine = pyttsx3.init()

def speak(name):
    engine.say(name)
    engine.runAndWait()