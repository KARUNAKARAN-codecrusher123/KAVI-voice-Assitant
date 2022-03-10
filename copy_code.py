from modules import *
import speech_recognition as sr
import pyttsx3
import sys

from email.mime import audio
from numpy import place
from setuptools import Command

mapping = {'play':play, 'listen':play, 'images':image, 'where is':locate,
    'locate':locate, 'wattsapp':whattsapp, 'open':open, 'weather':weather,
    'who is':info, 'search':info, 'movie review':info, 'history':info, 'get my ip':IP,
    'flip a coin':flip_a_coin, 'pick':lucky_no, 'choose':lucky_no, 'health of kavi':health
}
 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def take_command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            talk("listening.....")
            audio = r.record(source, duration=3)

            try:
                command = r.recognize_google(audio, language='en-in')
                print(f"user said:{command}\n")
                return command

            except Exception as e:
                talk("Pardon me,Please say that again")
                print("Pardon me,Please say that again")    
    return 


def choose(command):
    for key in mapping.keys():
        if key in command:
            return key, mapping[key]
    else:
        return '', talk


def func():
    talk("Tell me! How can I help you?")
    print("Tell me! How can I help you?")
    command = take_command().lower()
    if 'exit' in command or 'stop' in command or 'shutdown' in command or 'quit' in command:
        return False 
    else :
        key, task = choose(command)
        notdone =True
        while(notdone):
            
            if key=='':
                notdone = task(ques=command)
            elif key == 'images':
                # provide option in frontend instead ;-;
                print("""Please provide an option for Image
                    # 1, HD Random Picture
                    # 2, FHD Random Picture
                    # 3, 2K Random Picture
                    # 4, 4k Random Picture
                    # 5, Picture with User Provided Keywords """)
                talk("""Please provide an option for Image
                    # 1, HD Random Picture
                    # 2, FHD Random Picture
                    # 3, 2K Random Picture
                    # 4, 4k Random Picture
                    # 5, Picture with User Provided Keywords """)
                try:
                    ctx = None
                    type = int(take_command())
                    if type==5:
                        talk("speak keywords seperated by commas ")
                        ctx=take_command()
                except:
                    print("Sorry, couldn't register your choise. Please type it instead")
                    talk("Sorry, couldn't register your choise. Please type it instead")
                    try:
                        type = int(input())
                        if type==5:
                            talk("speak keywords seperated by commas ")
                            ctx=take_command()
                    except:
                        type = -1
                        print("not a valid choise")
                notdone = task(type, ctx)
            elif task == info:
                if key == 'search':
                    notdone = task(command.replace(key, ''), search=True)
                else :
                    notdone = task(command.replace(key, ''), summary=True)
            # no for whattsapp?
            elif key == 'whatsapp':
                notdone = task()
            elif key == 'weather':
                place = take_command()
                notdone = task(place)
            else:
                notdone = task(command.replace(key, '').lstrip())
        
        return True


if __name__ == '__main__':
    intro()
    x = True
    while x:  
        wishMe()
        x = func() 
    print("byee!!")
