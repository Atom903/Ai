import datetime
import os
import shutil
import subprocess
import time
import webbrowser
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
import wolframalpha
import json
import operator
import feedparser
import smtplib
import ctypes
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import random
import pywapi
import string

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Buongiorno!")

    elif hour >= 12 and hour < 18:
        speak("Buon pomeriggio !")

    else:
        speak("Buonasera !")

    assname = ("Vanya")
    #vanya
    speak("Sono la tua assistente Vanya")
    #speak(assname)


#def usrname():
 #   speak("Come dovrei chiamarti?")
  #  uname = takeCommand()
   # speak("Benvenuto"+uname)
    #speak(uname)
    #columns = shutil.get_terminal_size().columns

    #print("#####################".center(columns))
    #print("Benvenuto", uname.center(columns))
    #print("#####################".center(columns))

    speak("Come posso aiutarti?")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ascolto...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Riconoscimento...")
        query = r.recognize_google(audio, language='it-IT')
        print(f"Hai detto: {query}\n")

    except Exception as e:
        print(e)
        print("Non riesco a capirti, perdonami")
        return "None"

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    #tolgo tutti i comandi
    clear()
    wishMe()
    #usrname()
    username="Davide"
    while True:

        assname = ("vanya")
        query = takeCommand().lower()
        webbrowser.register('chrome', None)
        wikipedia.set_lang('it')

        #salvo tutti i comandi e poi li converto in lowercase per facilitare il riconoscimento
        if 'wikipedia' in query:
            speak('Cerco Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Come dice Wikipedia")
            print(results)
            speak(results)

        elif 'apri youtube' in query:
            speak("Vado su Youtube\n")
            webbrowser.open("https://www.youtube.it")
        elif 'cerca su youtube' in query:
            speak('cosa devo cercare?')
            cerca = takeCommand()
            url1= "https://youtube.it/results?search_query="
            completo= url1+cerca
            webbrowser.open(completo)


        elif 'apri google' in query:
            speak("Cerco Google\n")
            webbrowser.open("https://google.it")
        elif 'cerca su google' in query or 'su google' in query:
            speak("cosa vuoi che cerchi?")
            search=takeCommand()
            url1="https://google.it/search?q="
            gurl=url1+search
            webbrowser.open(gurl)

        elif 'chiudi google' in query: #DA TESTARE
                subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
                speak("chiuso\n")

        elif 'riproduci musica' in query:
            speak("cerco musica nel dispositivo")
            # music_dir = "G:\\Song"
            music_dir = r'C:\Users\Lenovo\Music'
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'che ore sono' in query:
            strTime = datetime.datetime.now().strftime("%H: %M")
            speak(f"Sono le: {strTime}")
            print(strTime)

        elif 'come stai' in query:
            speak("Non ho dei sentimenti, ma sono collegata ad una fonte di energia, quindi nel vostro linguaggio bene, grazie della premura")
            speak("Come sta lei singore?")

        elif 'bene' in query or "benissimo" in query:
            speak("Lieto di sentirlo")

        elif "cambia il mio nome in" in query:
            query = query.replace("cambia il mio nome in", "")
            assname = query

        elif "cambia nome" in query:
            speak("Come mi vorrebbe chiamare ")
            assname = takeCommand()
            speak("Accetto il nome da lei scelto")

        elif "come ti chiami" in query or "quale è il tuo nome" in query:
            speak("I miei dati dicono che mi chiamo"+assname)
            #speak(assname)
            print("I miei dati dicono che mi chiamo", assname)

        elif 'esci' in query or "spegni" in query:
            speak("Grazie del suo tempo")
            exit()

        elif "chi ti ha fatto" in query or "chi ti ha creato" in query:
            speak("Sono stata programmmata da Atom")

        elif 'scherza' in query or 'battuta' in query:
            speak(pyjokes.get_joke(language='it', category='all'))
        elif 'battuta su chuck norris' in query:
            speak(pyjokes.get_joke(language ='it', category= 'chuck'))
        elif "battuta nerd" in query:
            speak(pyjokes.get_joke(language='it', category='neutral'))



        elif "chi sono" in query:
            speak("se parli sei di sicuro un umano")

        elif "perchè sei al mondo" in query or "perchè esisti" in query:
            speak("Grazie ad atom, voleva fare un regalo ad aurora")

        elif "chi sei" in query:
            speak("Sono il tuo assistente vocale")

        elif 'spegni il computer' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'svuota il cestino' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Ho riciclato tutto")

        elif "non ascoltare" in query or "silenziati" in query:
            speak("Per quanti secondi devo sospendrmi?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "dov'è" in query or "dove si trova" in query:
            query = query.replace("dov'è", "")
            location = query
            speak("Localizzo")
            speak(location)
            webbrowser.open("https://www.google.it/maps/place/"+ location +"")

        elif "prendi nota" in query:
            speak("Cosa devo scrivere signore?")
            note = takeCommand()
            file = open('oblivion_note.txt', 'w')
            speak("devo includere data e ora")
            snfm = takeCommand()
            if 'si' in snfm or 'certo' in snfm:
                strTime = datetime.datetime.now().strftime("%H: %M")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "leggimi la nota" in query or "leggi la nota" in query:
            speak("Mostro la nota")
            file = open("oblivion_note.txt", "r")
            print(file.read())
            speak(file.read(6))


        elif "meteo" in query or "che tempo fa" in query:
            # Google meteo da open weather
            #api_key = "Api key"
            speak("Attualmente posso solo aprire la pagina dedicata. Mi appoggio a ilmeteo.it")
            speak(" Quale città ")
            print("città: ")
            city_name = takeCommand()
            base_url = "http://ilmeteo.it/meteo/"
            complete_url = base_url + city_name
            webbrowser.open(complete_url)
        ###########################DA TESTARE##########################################################################################
        #elif "test" in query:
            #speak("quale città")
            #city=takeCommand()
            #loc_id= pywapi.get_location_ids(city)
            #result= pywapi.get_weather_from_weather_com('loc_id')
            #print("dice:"+ string.lower(result['current_conditions']['text']) + "e" + result['current_conditions']['temperature'] + "C")
        ###############################################################################################################################
        elif "Buongiorno" in query:
            speak("Un caldo" + query)
            speak("Come sta signore?")
            speak(assname)
        elif "camera" in query or "fammi una foto" in query:
            ec.capture(0, "Vanya Camera", "Vanya.jpg")
        elif "cosa è" in query or "chi è" in query:

            # Use the same API key
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("Nessun risultato")

    # elif "" in query:
    # Command go here
    # For adding more commands
