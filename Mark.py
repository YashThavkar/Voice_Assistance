import time 
import pyttsx3
import datetime
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
from PyDictionary import PyDictionary
import pywhatkit
import sys
import pyautogui
import requests
import instaloader
from keyboard import press_and_release


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = datetime.datetime.now()

    if hour >=0 and hour <=12:
        speak(f"Good Morning Sir ")
        print(f"Good Morning Sir , its {tt}")

    elif hour>=12 and hour <=18:
        speak (f" Good Afternoon Sir ")
        print(f" Good Afternoon Sir , its {tt}")

    else:
        speak(f"Good Evening Sir ")
        print(f"Good Evening Sir , its {tt}")


    speak(" Mark this side , how may i help you ")

def  takeCommand():
      #It take microphone  input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language="en.in")
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)

        print("Pardon.... i dont get it")
        speak("Pardon.... I Don't get it")
        return ("None")
    return query



if __name__ =="__main__":
    wishMe()
    while True:


        query =takeCommand().lower()

        #logic building task

        if 'open command prompt' in query:
            os.system("start cmd")
            speak("Opening command prompt")


        elif 'be my girlfriend' in query:
            speak("sir , i am your friend and i know how you are feeling but its time to work , just keep your emotions inside and we will get back to work")

        elif "emotion" in query:
            speak(" Ya ,I know and can understand your feeling for your girlfriend , by the way you haven't told me you have girlfriend")

        elif "don't have a girlfriend" in query:
            speak("ya the same think  i was think for , you haven't let me know....")

        elif " your favorite food" in query:
            speak("actually , i like to eat data....")

        elif" tell me about education" in query :
            speak ("ya , sure but about which branch , just like B.Tech , MBBS , BBA , BSC(Computer Science) , BSC(Agriculture) , LLB ,BALLB and many courses")

        elif ' idiot' in query:
            speak ("no sir , i am not an idiot , actually the problem is your microphone is cheap ,because of the same i am not able to recognize...")






#time for alarm
        elif 'set alarm' in query:
            dt =int(datetime.datetime.now().hour)
            if dt==22:
                music_dir ="D:\\mobile\\download\\snaptube\\download\\SnapTube Audio"
                songs =os.listdir(music_dir)
                os.starfile(os.path.join(music_dir , songs[0]))
                speak("alarm has been set...")


        elif 'open webcam' in query:
            cap =cv2.VideoCapture(1)
            while True:
                ret, img =cap.read()
                cv2.imshow("C:\\Program Files (x86)\\Iriun Webcam" , img)
                k= cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyedAllWindows()

        elif 'music offline' in query or 'songs offline' in query:
            speak("Playing music offline")
            music_dir ="D:\\mobile\\download\\snaptube\\download\\SnapTube Audio"
            songs =os.listdir(music_dir)
            rd =random.choice(songs)
            #if there are many files in same folder and only want to deal with mp3
            #for song in songs:
                #if song.endwith('.mp3'):
            os.startfile(os.path.join(music_dir ,rd))


        elif" ip address" in query:
            ip = get('https://api.ipify.org').text
            print( f'Your IP Adrress is : {ip} ')
            speak(f"Your IP Address is {ip} ")



        elif "wikipedia" in query:
            try:
                speak ("Searching wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                speak(results)
                print(results)

            except Exception as e:
                speak ("Sorry sir, there is some issue  while i am searching word , if it is not working  just use webbrowser")



        elif "open youtube" in query:
            speak ("opening youtube")
            webbrowser.open('www.youtube.com')


        elif "instagram" in query:
            speak ("opening instagram")
            webbrowser.open('www.instagram.com')


        elif "whatsapp" in query:
            speak ("opening watsapp")
            webbrowser.open('https://web.whatsapp.com/')



        elif "github" in query:
            speak ("opening github")
            webbrowser.open('https://github.com/YashThavkar')



        elif "gmail" in query:
            speak ("opening gmail")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')



        elif "open official mail" in query:
            speak ("opening Gmail official")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')


        elif "maps" in query:
            speak ("opening google maps")
            webbrowser.open('https://www.google.com/maps/@21.0130938,79.3664375,17.86z')



        elif "googlelab" in query:
            speak ("opening quick Lab")
            webbrowser.open('https://go.qwiklabs.com/qwiklabs-express-2021?utm_source=medium&utm_medium=blog&utm_campaign=Qwiklabs+Express+blog')


        elif "colab" in query:
            speak("opening google colab")
            webbrowser.open('https://colab.research.google.com/drive/1jrE-6Ar-Dy1ea1n0WsxwjUt48HEbpQy9#scrollTo=s_e2S288xSIV')


        elif "jupyter" in query:
            speak("opening jupyter notebook")
            webbrowser.open('http: // localhost: 8888 / tree')




        elif 'fact' in query:
            list = ["Turtles have no teeth.", "Prehistoric turtles may have weighed as much as 5,000 pounds.",
                    "Only one out of a thousand baby sea turtles survives after hatching.",
                    " Sea turtles absorb a lot of salt from the sea water in which they live. They excreteexcess salt from their eyes, so it often looks as though they'recrying.",
                    "Helium is a colourless, odourless, tasteless inert gas at room temperature and makes upabout 0.0005% of the air we breathe.",
                    "Helium Balloon Gas makes balloons float. Helium is lighter than air and just as theheaviest things will tend to fall to the bottom, the lightest thingswill rise to the top.",
                    'Helium Balloon Gas makes balloons float. Helium is lighter than air and just as theheaviest things will tend to fall to the bottom, the lightest thingswill rise to the top.',
                    'Camels can spit.', 'An ostrich can run 43 miles per hour (70 kilometers per hour).',
                    'Pigs are the fourth most intelligent animal in the world.',
                    'Dinosaurs didnt eat grass? There was no grass in the days of the dinosaurs.',
                    'India has the most post offices in the world',
                    'Navigation is derived from the Sanskrit word NAVGATIH',
                    ' The word navy is also derived from the Sanskrit word Nou.',
                    ' Until 1896, India was the only source for diamonds to the world',
                    'The place value system and the  decimal system were developed in 100 BC in India.',
                    'A snail can sleep for 3 years.',
                    'The names of the continents all end with the same letter with which they start.',
                    'Twenty-Four- Karat Gold is not pure gold since there is a small amount of copper init. Absolutely pure gold is so soft that it can be molded with thehands.',
                    'Paris, France has more dogs than people.',
                    'New Zealand is home to 70 million sheep and only 40 million people.',
                    'A frog named Santjie, who was in a frog derby in South Africa jumped 33 feet 5.5inches.',
                    'The longest life span of a frog was 40 years.',
                    'The eyes of a frog flatten down when it swallows its prey.',
                    'The name India is derived from the River Indus.', 'The Persian invaders converted it into Hindu',
                    'The name Hindustan combines Sindhuand Hindu and thus refers to the land of the Hindus.',
                    ' Chess was invented in India.',
                    'The place value system and the decimal system were developed in 100 BC in India.',
                    'The game of snakes & ladders was created by the 13th century poet saint Gyandev. Itwas originally called Mokshapat.',
                    ' The ladders in the game represented virtues and the snakes indicated vices.']
            rd = random.choice(list)
            speak(rd)
            print(rd)


        elif "open spotify" in query:
            speak("opening spotify")
            webbrowser.open('https: // open.spotify.com /?nd = 1')


        elif "open google" in query:
            speak('sir,opening google')
            webbrowser.open(f'https://www.google.com')

        elif "new tab" in query:
            press_and_release('Ctrl +t')
            speak('opening new tab')

        elif 'close tab' in query:
            press_and_release('Ctrl+w')
            speak('closing tab')

        elif 'new window' in query:
            press_and_release('Ctrl+n')
            speak('opening new window')

        elif'downloads' in query:
            press_and_release('Ctrl+j')
            speak('opening downloads')

        elif 'history' in query:
            press_and_release('Ctrl+h')
            speak('opening history')

        elif 'bookmark' in query:
            press_and_release('Ctrl+d')
            press_and_release('enter')
            speak('saving in bookmark')

        elif'incognito' in query:
            press_and_release('Ctrl+Shift + n')
            speak('opening incognito')

        elif 'switch tab' in query or 'change tab' in query:
            try:
                tab =query.replace("switch tab" ,"")
                cn=tab.replace("switch tab", " ")

                num =cn
                pn = f'ctrl+{num}'
                press_and_release(pn)
                speak(f"switching tab to number {cn}")

            except Exception as e:
                speak("i haven't get it.... you can repeat")


        elif "close all tabs" in query:
            press_and_release('ctrl+shift+w')
            speak("closed all the tabs")


        elif "open webbrowser" in query:
            speak('sir , what should i search on webbrowser')
            cn =takeCommand().lower()
            webbrowser.open(f'{cn}')

        elif "meaning" in query:
            speak("opening Dictionary")
            speak('which words meaning you want to find')
            cn =takeCommand().lower()
            dict = PyDictionary()
            meaning = dict.meaning(f"{cn}")
            speak(meaning)
            print(meaning)


        elif "watsapp message to fazle" in query:
            speak("trying to send message to fazle")
            pywhatkit.sendWhatmsg("=919168921472", "You will be always my best friend", 2.30)



        elif " watsapp message to bestie" in query:
            speak("trying to send message to bestie")
            pywhatkit.sendWhatmsg("=918766445708", "You will be always my best friend", 3.19)


        elif "songs on youtube" in query or "song on youtube" in query:
            speak('sir , which song you want to search on youtube')
            cn = takeCommand().lower()
            pywhatkit.playonyt(cn)
            speak(f"playing {cn} on youtube")
            time.sleep(15)


        #elif "mail to inayat" in query:
        #        try:
        #        speak("What should i text him ?")
        #        content = takeCommand().lower()
        #        to = "fazlehasan333@gmail.com"
        #        sendEmail(to, content)
        #        speak("Email has been send to fazle")

        #    except Exception as e:
        #        print(e)
        #        speak("sorry sir, I am not able to connect with  inayat at this moment ")


#code for closing tabs
        elif "close command prompt" in query:
            speak("Okay Sir , closing command prompt")
            os.system("taskkill /f /im cmd.exe")


        elif "sleep mode" in query:
            speak ("lappy is in sleep mode")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


        elif  "switch tab" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')


        elif "news" in query:
            speak ("Please wait sir,  i am feteching the latest news for you")
            webbrowser.open('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')
            time.sleep(15)


        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            ipAdd =requests.get('https://api.ipify.org').text
            print(ipAdd)

            speak(f'sir  i have foundout some information about , country name , state name , city name , and many other info , you can just go through it')
            webbrowser.open('https://get.geojs.io//v1//ip//geo.json')
            time.sleep(15)


        elif "instagram profile " in query or "profile of instagram" in query:
            speak("Sir ,please Enter the user name correctly")
            name =input("Enter the username :-  ")
            webbrowser.open(f'www.instagram.com/{name}')
            speak(f"Sir , here is profile of user {name}")
            time.sleep(2)
            speak("Sir would you like to download the profile picture of this account")
            condition =takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I have downloaded it sir, Profile picture is saved in the system , Ready for other work")


        elif "take a screenshot" in query or "screenshot" in query:
            speak("Sir , Please tell me the name for this screenshot file")
            name= takeCommand().lower()
            speak("hold on man , taking a screenshot" )
            time.sleep(1.5)
            img =pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir , the screenshot is save in system , Reminder , all the images are saved in pycharm project file")

        elif " online" in query or "online help" in query or "online tasks" in query:
            speak("Hello sir , i am jarvis ,  i can handle 50 percent of your System with your   voice command, i will just note down all the tasks which I can perform ")

            print("Trying to find IP Adrress :- say ip adrress")
            speak("Trying to find IP Adrress :- say ip adrress")

            print("Trying to search on wikipedia :-say wikipedia")
            speak("Trying to search on wikipedia :-say wikipedia ")

            print("To open google :- say open google ")
            speak("To open google :- say open google ")

            print("To open YouTube :- say open youtube")
            speak("to open youtube :- say open youtube")

            print("To open Instagram :- say open instagram ")
            speak("To open instagram :- say open instagram ")

            print("To open WatsApp :- say open watsapp ")
            speak("To open watsapp :- say open watsapp  ")

            print("To open github :- say open github ")
            speak("To open github :- say open github  ")

            print("To open googlemaps :- say open maps")
            speak("To open googlemaps :- say open maps ")

            print("To open colab :- say open colab ")
            speak("To open colab :- say open colab ")

            print("To open jupyter notebook:- say open jupyter ")
            speak("To open jupyter notebook:- say open jupyter ")

            print("To open spotify :- say open spotify ")
            speak("To open spotify :- say open spotify  ")

            print("To play songs on youtube :- say songs on youtube ")
            speak("To play songs on youtube :- say songs on youtube ")

            print("trying to update yourself with news :- Say news ")
            speak("trying to update yourself with news :- Say news ")

            print("to find your city or location :- say where i am ")
            speak("to find your city or location :- say where i am ")

            print("To download instagram profile :- say instagram profile ")
            speak("To download instagram profile :- say instagram profile  ")

            speak("this all command will be only perform while you are connected with network")

            time.sleep(10)


        elif " offline" in query or "offline help" in query or "offline task" in query:
            speak("Hello sir , i am jarvis ,  i can handle 50 percent of your System with your   voice command, i will just note down all the tasks which I can perform ")
            print("To Ask Fact :- say Fact ")
            speak("To Ask Fact :- say Fact ")

            print("To set Alarm :- say set Alarm")
            speak("To set Alarm :- say set Alarm ")

            print("To Play Music Offline  :- say Music Offline ")
            speak("To Play Music Offline  :- say Music Offline ")

            print("To find Meaning of the word :- say Meaning ")
            speak("To find Meaning of the word :- say Meaning  ")

            print("To open Command Prompt :- say Open Command Prompt  ")
            speak("To open Command Prompt :- say Open Command Prompt  ")

            print("To close Command Prompt :- say close Command Prompt ")
            speak("To close Command Prompt :- say close Command Prompt ")

            print("If you want to switch the tab :- Just say Switch Tab ")
            speak("If you want to switch the tab :- Just say Switch Tab ")

            print("If you want to take ScreenShot :- Just say take a ScreenShot ")
            speak("If you want to take ScreenShot :- Just say take a ScreenShot ")

            print("If you want to turn on Sleep Mode :- Just say Sleep Mode ")
            speak("If you want to turn on Sleep Mode :- Just say Sleep Mode ")


            speak("this all commands or tasks can be perform offline , you can use it anytime ")
            time.sleep(10)

        elif "go to sleep" in query or 'thanks' in query:
            speak("Thanks for being with me sir , Have a good day")
            break
            sys.exit()

