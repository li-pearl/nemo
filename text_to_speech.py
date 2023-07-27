import pyttsx3
#pyttsx3-2.71

engine = pyttsx3.init()

def speak(name):
    engine.say(name)
    engine.runAndWait()