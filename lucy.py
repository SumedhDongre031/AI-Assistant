import pyttsx3 
import pywhatkit
import datetime
from random import randrange
import speech_recognition as sr
import wikipedia
import pyjokes

listener = sr.Recognizer() #it will listen to our command and blah blah
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[3].id)
# engine.setProperty("rate", 1.0 )

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("I am Lucy. It's Nice to meet you!")
talk("What can I do for you?")

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "lucy" in command:
                print(command+" (INSIDE TRY BLOCK)")
                command = command.replace("lucy", "")
                # talk(command)
    except:
        print("EXCEPT BLOCK")
    return(command)
# print(take_command())

def run():
    command = take_command()
    # print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        print(command)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif " who is" in command:
        person = command.replace("Who is", "")
        print(person)
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "wikipedia" in command:
        person = command.replace("wikipedia", "")
        print(person)
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif "are you single" in command:
        talk("oh! sorry!, i am in a relationship with wifi")
    elif "date" in command:
        talk("oh No!, Not again")
    elif "can i get your number" in command:
        talk("Sorry i have a boyfriend!")
    elif "do you have a boyfriend" in command:
        talk("yes i am in a relationship with wifi")
    elif "bye" in command:
        print(command)
        talk("Oh! you are leaving, See you Next time!")
        return("quit")
    else:
        talk("sorry! I didn't heard you.")

while True:
    end = run()
    if end == "":
        pass
    elif end =="quit" :
        break