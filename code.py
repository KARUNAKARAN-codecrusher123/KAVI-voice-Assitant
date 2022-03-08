from email.mime import audio
from ipaddress import ip_address
from numpy import place
from setuptools import Command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import webbrowser
from datetime import datetime
from geopy.geocoders import Nominatim
import os
import psutil
from bs4 import BeautifulSoup
import requests





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


hi = 0

if hi == 0:
    talk('hello iam kkavi')
    print('hello iam kavi Voice assistant')
    talk('How are you buddy!!!')
    print('How are you buddy!!!')
    talk('doing good right?????')
    print('doing good right?????')
    talk('think so good')
    print('think so good')
    talk('what can i do for you buddy')
    print('what can i do for you buddy')
else:
    print('listening')


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        talk("listening.....")
        audio=r.record(source,duration=3)

        try:
            command=r.recognize_google(audio,language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:
            talk("Pardon me,Please say that again")
            print("Pardon me,Please say that again")    
            return "Not Found"
            print("command")
        return command


print("Loading your AI personal Assistant kavi")
talk("Loading your AI personal Assistant kavi")


if __name__=='__main__':


    while True:
        talk("Tell me Sir! How can I help you?")
        print("Tell me Sir! How can I help you?")
        command=take_command().lower()

        if "exit" in command or "stop" in command or "shutdown" in command:
            talk("Your AI assistant kavi is shutting down,Good bye Sir and have a good day (:")
            print("Your AI assistant kavi is shutting down,Good bye Sir and have a good day (:")
            break

        elif 'play' in command:
            talk('playing')
            print('playing')
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'whatsapp' in command:
            pywhatkit.sendwhatmsg("+91 93611 40968", "hello iam kavi,my boss has told me to text any important info",
                              13, 58)
            print("Successfully Sent!")
            continue

        elif 'who is' in command:
           person = command.replace('who is', '')
           source = wikipedia.summary(person, 100)
           print(source)
           talk(source)


        elif 'search' in command:
            info = command.replace('search', '')
            general = wikipedia.search(info, 100)
            print(general)
            talk(general)   

        elif 'history' in command:
            gen = command.replace('history, battle, movie review', '')
            small = wikipedia.summary(gen, 100)
            print(small)
            talk(small)            


        elif 'health' in command:
            load1, load5, load15 = psutil.getloadavg()
            cpu_usage = (load15 / os.cpu_count()) * 100
            cd = ("My health was in good condition because your'e using me in good way (cpu usage) : ", cpu_usage)
            talk(cd)

        elif 'memory' in command:
            bc = (psutil.virtual_memory()[2])
            talk(bc)
            
        elif 'location' in command:
            loc = Nominatim(user_agent="GetLoc")
            getloc = loc.geocode("Coimbatore")
            print(getloc.address)
            talk(getloc)

        elif 'movie review' in command:
            movie = command.replace('movie review', '')
            small = wikipedia.summary(movie, 10)
            print(small)
            talk(small)

        elif 'are you single' in command:
            talk('no......um.i am in relationship with wireless devices')
        elif 'do you like me' in command:
            talk('yes boss definitely')
        elif 'what is your name' in command:
            talk('My devloper karunakran has named me kkavi')
        elif 'cringe' in command:
            talk('alright........he/she was funniest perosn')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        elif 'get my ip' in command:
            ip_address=requests.get('https://api64.ipify.org?format=json').json()
            ip=ip_address
            print(f'Your ip address is :- {ip["ip"]}')
            talk(f'Your ip address is :- {ip["ip"]}')
            
            
           

        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            talk("User asked to Locate")
            talk(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            
        elif "weather" in command:
            api_key="51d5d78391e312e72cde67174f38e770"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            talk("which city are you looking to know")
            place=take_command()
            complete_url=base_url+"appid="+api_key+"&q="+place
            result = requests.get(complete_url)
            x=result.json()
            if x["cod"]!="404":
                y=x["main"]
                city_temperature = y["temp"]
                city_humidiy = y["humidity"]
                ans = x["weather"]
                weather_description = ans[0]["description"]
                talk("Temperature" + str(place) +"in kelvin unit is " +
                      str(city_temperature) +
                      "\n humidity in percentage is " +
                      str(city_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print( str(place) +" Temperature in kelvin unit = " +
                      str(city_temperature) +
                      "\n humidity (in percentage) = " +
                      str(city_humidiy) +
                      "\n description = " +
                      str(weather_description))


        
        
    

    
    
