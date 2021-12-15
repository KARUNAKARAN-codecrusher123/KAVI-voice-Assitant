# CindrellaVoiceAssistant
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


hi=0

if hi==0:
    talk('hello iam cindrella')
    print('hello iam cindrella')
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
    try:
        with sr.Microphone() as source:
            talk('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'cindrella' in command:
                command = command.replace('cindrella', '')
                print(command)
    except:
        pass
    return command


def run_cindrella():
    command = take_command()
    print(command)
    if 'play' in command:
        talk('playing')
        print('playing')
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'whatsapp' in command:
        pywhatkit.sendwhatmsg("+91 93611 40968", "hello iam cindrella,my boss has told me to text any important info",
                              13, 58)
        print("Successfully Sent!")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        source = wikipedia.summary(person, 100)
        print(source)
        talk(source)
    elif 'search' in command:
        info = command.replace('search', '')
        general = wikipedia.search(info, 10)
        print(general)
        talk(general)
    elif 'history' in command:
        gen = command.replace('history, battle, movie review', '')
        small = wikipedia.summary(gen, 10)
        print(small)
        talk(small)
    elif 'movie review' in command:
        movie = command.replace('movie review', '')
        small = wikipedia.summary(movie, 10)
        print(small)
        talk(small)
    elif 'are you single' in command:
        talk('no......um.i am in relationship with wireless devices')
    elif 'do you like me' in command:
        talk('yes boss definitely')
    elif 'cringe' in command:
        talk('alright........her name is janani,she was greatest,legend and gethu janani,foodie and more,her petname is cringe child')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk('cant get it....please say it again')


while True:
    run_cindrella()
