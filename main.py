import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine=ttx.init()
voice=engine.getProperty('voices')
engine.setProperty('voice','french')

def parler(text):
    engine.say(text)
    engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("parlez maintenant")
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language='fr-FR')
            command.lower()
    except:
        pass
    return command

parler("Bonjour Robert, je suis ton assistant, que puis-je faire pour t'aider aujourd'hui")
def lancer_assistant():
    command=ecouter()
    print(command)
    if 'mets une chanson de' in command:
        chanteur=command.replace('mets la chanson de','')
        print(chanteur)
        parler("D'accord, un instant et je vous mets la chanson")
        pywhatkit.playonyt(chanteur)

    elif 'heure' in command:
        heure=datetime.datetime.now().strftime('%H:%M')
        parler('il est'+heure)

    elif 'cherche des informations' in command:
        donne=command.replace('cherche des informations','')
        print(donne)
        pywhatkit.search(donne)
    elif 'quels sont' in command:
        rech=command.replace('quels sont','')
        parler(rech)
        pywhatkit.search(rech)
    elif 'quelles sont' in command:
        tr=command.replace('quelles sont','')
        parler(tr)
        pywhatkit.search(tr)
    elif 'quelle est' in command:
        re=command.replace('quelle est','')
        parler(re)
        pywhatkit.search(re)
    elif 'quel est' in command:
        ans=command.replace('quel est','')
        parler(ans)
        pywhatkit.search(ans)
    elif 'Bonjour' in command:
        parler('bonjour,ca va?')
    else:
        parler('je ne comprends pas')

while True:
    lancer_assistant()