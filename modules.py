import os
import subprocess
from PIL import Image
import wikipedia
import pywhatkit
import pyttsx3
import webbrowser
import requests
import psutil
import pyjokes
import datetime
import random


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text=None, ques=None):
    if text==None:
        if(ques!=None):  
            # talk to kavi like a buddy :)

            if 'are you single' in ques :
                engine.say('no......um.i am in relationship with wireless devices')
            elif 'do you like me' in ques:
                engine.say('yes boss definitely')
            elif 'what is your name' in ques:
                engine.say('My devloper karunakran has named me kkavi')
            elif 'cringe' in ques:
                engine.say('alright........he/she was funniest perosn')
            elif 'joke' in ques:
                joke = pyjokes.get_joke()
                print(joke)
                engine.say(joke)
            elif 'i am tired' in ques:
                engine.say('you should take a break')
            elif 'favorite game' in ques:
                engine.say('my favorite game is chess')
            elif 'can you dance' in ques:
                engine.say('I cant dance as of now, but I can play some dance music')
            elif 'how do i look' in ques:
                engine.say('juding from your voice, amazing')
            elif 'can you cook' in ques:
                engine.say('i can cook you up amazing bedtime stories if you want')
            elif 'who is your friend' in ques:
                engine.say('her name is nilla voice assistant, she was in another repository')
        
    else :
        engine.say(text)
    engine.runAndWait()
    return False


def image(type, ctx=None):
    if (type>5 or type<=0):
        return True 
    elif type ==5:
        ctx.replace("comma", ',')
        txt = '?'+ctx
    else: 
        list1 = ['1280x720', '1920x1080', '2048x1080', '5096x2160']
        txt = list1[type-1]
    response = requests.get("https://source.unsplash.com/random/{0}".format(txt))
    file = open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close
    return False


def play(song, genre=None, artist=None, lyrist=None):
    if song=="random":
        # code for getting genre/artist/lyrist etc
        # and generating a random playlist.
        # ask if user would like a song or on loop(playlist).
        pass
    else:
        talk("playing your requested song "+song+", please wait!")
        print("playing",song)
        pywhatkit.playonyt(song)
    return False


def info(text, search=False, summary=False, line =10, wordCount=100):
    if(search):
        information = wikipedia.search(text, wordCount)
    elif(summary):
        information = wikipedia.summary(text, line)
    print(information)
    talk(information)
    return False


def whattsapp(no="+91 93611 40968"):
    pywhatkit.sendwhatmsg(no, "hello iam kavi,my boss has told me to text any important info",13, 58)
    print("Successfully Sent!")
    return False


def locate(place):
    talk("user asked to locate "+place)
    webbrowser.open("https://www.google.nl/maps/place/" + place + "")
    return False


def open(file):
    if file == 'calculator':
        subprocess.call("calc.exe")
    else:
        try:
            link = str(file).upper()+".EXE"
            os.startfile(link)
        except:
            talk("could not open the file {file}")
    return False


def weather(location):
    api_key = "51d5d78391e312e72cde67174f38e770"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location
    result = requests.get(complete_url)
    x = result.json()
    if x["cod"] != "404":
        weather = x["main"]
        talk("Temperature of " + str(location) + " in kelvin unit is " +
            str(weather['temp']) +
            "\n humidity in percentage is " +
            str(weather['humidity']) +
            "\n description  " +
            str(x['weather'][0]['description']))

        print(str(location) + " Temperature in kelvin unit = " +
            str(weather['temp']) +
            "\n humidity (in percentage) = " +
            str(weather['humidity']) +
            "\n description = " +
            str(x['weather'][0]['description']))
    else: 
        talk("Sorry, there was some error. Please try again later or look for the weather of a different location")
        print("Sorry, there was some error. Please try again later or look for the weather of a different location")
    return False


def health(ctx):
    pid = os.getpid()
    py = psutil.Process(pid)
    memory_use = py.memory_info()[0] / 2. ** 30
    talk("I use {0:.2f} GB..".format(memory_use))
    return False


def IP(ctx):
    ip_address=requests.get('https://api64.ipify.org?format=json').json()
    ip=ip_address
    print(f'Your ip address is :- {ip["ip"]}')
    talk(f'Your ip address is :- {ip["ip"]}') 
    return False


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
       talk("Good Evening!") 
    return 


def flip_a_coin(ctx):
    mapping = {0:'head', 1:"tail"}
    key = random.randint(0,1)
    talk(f"It's a {mapping[key]} pal!")
    print(f"It's a {mapping[key]} pal!")
    return False


def lucky_no(ctx):
    num = random.randint(1,10)
    print(f"{num} is your lucky number.")
    talk(f"{num} is your lucky number.")
    return False


def intro():
    print('hello iam kavi Voice assistant')
    talk('hello iam kavi')
    print('How are you buddy!!!')
    talk('How are you buddy!!!')
    print('doing good right?????')
    talk('doing good right?????')
    print('think so good')
    talk('think so good')
    print('what can i do for you buddy')
    talk('what can i do for you buddy')
    talk("")
    return 
