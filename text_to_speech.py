import pyttsx3
#pyttsx3-2.71

engine = pyttsx3.init()

engine.say("Anshi")
engine.runAndWait()

def speak(name):
    engine.say(name)
    engine.runAndWait()