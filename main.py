import speech_recognition as sr
import pyttsx3, pywhatkit,datetime,pyjokes, wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(something):
    engine.say(something)
    engine.runAndWait()
def take_command():
    with sr.Microphone() as source:
        print('listening')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        talk(command)
    return command

def run():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        talk("Current time is "time)
        print(time)

    elif "who the hell is" in command:
        person = command.replace("who the hell is",'')
        info = wikipedia.summary(person,1)
        talk(info)
        print(info)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    else:
        talk("I didnt get what you want to say , Please say again")

while True:
    run()

