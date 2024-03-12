import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
from time import sleep
import pyautogui
from pynput.keyboard import Key,Controller
import random
import webbrowser
import speedtest


from plyer import notification
from pygame import mixer
import speedtest
 
for i in range(3):
    a=input("Enter Password to open :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")


from INTRO import play_gif
play_gif


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone()as source:
        print("Listning....")
        r.pause_threshold= 1
        r.energy_threshold = 300
        audio=r.listen(source,0,4)
        try:
            print("Understandinig...")
            query=r.recognize_google(audio,language='en-in')
            print(f"you said:{query}\n")
        except Exception as e:
            print("say that again")
            return "none"
        return query
    
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
    
if __name__ == "__main__":
    while True:
        query= takeCommand().lower()
        if "wake up" in query:
            from Gretme import greetMe
            greetMe()

            while True:
                query=takeCommand().lower()
                if"go to sleep"in query:
                    speak("ok sir , you can call me anytime")
                
                elif"change password"in query:
                    speak("what's the new password")
                    new_pw=input("enter the new password\n")
                    new_password=open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks=[]
                    speak("do you want to clear old tasks (plz speak yes or no)")
                    query=takeCommand().lower()
                    if "yes"in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()                

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )

                elif "start"in query:
                    query=query.replace("srart","")
                    query= query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")


                elif "play a game" in query:
                    from game import game_play
                    game_play()
                  
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")


                elif "screenshot"in query:
                    import pyautogui 
                    im = pyautogui.screenshot()
                    im .save("ss.jpg")

                # elif"internet speed"in query:
                #     wifi= speedtest.speedtest()
                #     upload_net= wifi.upload()/1048576   #1024*1024 bytes
                #     download_net=wifi.download()/1048578
                #     print("wifi upload speed",upload_net)
                #     print("wifi download speed",download_net)
                #     speak("wifi download speed is {download_net}")
                #     speak("wifi upload speed is {upload_net}")
                    



                elif "hello" in query:
                    speak("hello sir,how are you ?")
                elif"i am fine"in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect sir")
                elif"thank you"in query:
                    speak("you are Welcome, sir")
                elif "good"in query:
                    speak("Thank you sir!")
               

                elif " shri ram" in query:
                    speak("jai shri ram sir")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif"close"in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()

                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()                

                elif"google"in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif"youtube"in query:
                    from SearchNow import searchyoutube
                    searchyoutube(query)

                elif"wikipedia"in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "tired" in query:
                    speak("playing your favourite song, sir")
                    a= (1,2,3,4,5,6,7)
                    b= random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=se9DDAwwGQY")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=KEkuSubnZMs")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=oRGhqUjWF6U")
                    elif b==4:
                        webbrowser.open("https://www.youtube.com/watch?v=VAdGW7QDJiU")
                    elif b==5:
                        webbrowser.open("https://www.youtube.com/watch?v=GvXDq-P1NB8")
                    elif b==6:
                        webbrowser.open("https://www.youtube.com/watch?v=ue1B35u2cBE")
                    elif b==7:
                        webbrowser.open("https://www.youtube.com/watch?v=5DK-ZWyxZ8k")


                # elif"news"in query:
                #         from NewsRead import latestnews
                #         latestnews()
                # elif " WhatsApp"in query:
                #     from Whatsapp import sendMessage
                #     sendMessage()

                elif "temperature" in query:
                    search="temreature in chhattisgarh"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div", class_ = "BNeawe").text
                    speak(f"current{search}is{temp}")

                elif "weather" in query:
                    search="temreature in chhattisgarh"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div", class_ = "BNeawe").text
                    speak(f"current{search}is{temp}")

                
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")                

                elif "the time" in query:
                  strtime = datetime.datetime.now().strftime("%H:%M")    
                  speak(f"Sir, the time is {strtime}")
                elif "finally sleep" in query:
                    speak("going to sleep ,sir bye bye ")
                    exit()

                elif "remember that" in query:
                   rememberMessage = query.replace("remember that","")
                   rememberMessage = query.replace("jarvis","")
                   speak("You told me to "+rememberMessage)
                   remember = open("Remember.txt","a")
                   remember.write(rememberMessage)
                   remember.close()
                elif "what do you remember" in query:
                   remember = open("Remember.txt","r")
                   speak("You told me to " + remember.read())
                 
                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown ")
                    shutdown=input("do you wish to shutdown your computer? (yes/no)")
                    if shutdown=="yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown=="no":
                        break

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\panka\\OneDrive\\Desktop\\ai.py - Copy\\FocusMode.py")
                        exit()

                    
                    else:
                        pass
                    

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                # elif "translate" in query:
                #     from Translator import translategl
                #     query = query.replace("jarvis","")
                #     query = query.replace("translate","")
                #     translategl(query)
                

                    




               

