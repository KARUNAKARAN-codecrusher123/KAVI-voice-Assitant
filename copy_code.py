import modules
import speech_recognition as sr
import pyttsx3
 
 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


