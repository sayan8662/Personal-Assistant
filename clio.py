import pyttsx3 # text-to-speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import sys
import webbrowser
import os
import cv2
import requests
from requests import get
import pywhatkit as kit
import pyjokes
import pyautogui # for interacting
import time 
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase 
import smtplib
import pytz
import geocoder
import instaloader
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import pyowm



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today is..")
    speak(day)
    speak(month)
    speak(year)
    
    
def wishme():
    speak("Welcome back sir! Hope you are having a great day so far...")
    time()
    date()
    hour = datetime.datetime.now().hour
    
    if hour >= 5 and hour < 12:
        speak("Good Mornig sir...!")
        
    elif  hour >= 12 and hour < 16:
        speak("Good Afternoon sir...!")
        
    elif hour >= 16 and hour < 23:
        speak("Good Evening sir...!")
        
    else:
        speak("Good Night sir...!")
        
    speak("I am CLIO 1.32, your personal virtual assistant, at your service sir! Please say how may I help you!")
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}" )
        
    except Exception as e:
        print(e)
        # speak("SORRY sir! I can't get you, please say it again...")
        return "None"
    query = query.lower()
    return query


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f71e912b8208406c856a68373cb630b5'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "nineth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
        
        
def pdf_read():
    book = open('PythonForDummies.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Sir, please enter the page number from which you want me to read")
    pg = int(input("Please enter the page number here:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    book.close()
    
    
def TaskExecution():
    
    wishme()
    
    while True:
        
        query = takeCommand()
        
        if 'time' in query:
            time() 
            
            
        elif 'date' in query:
            date()     
            
            
        elif 'wikipedia' in query:
            speak("Searching wikipedia...just a moment!")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query)
            print(result)
            speak(result)  
            
            
        elif 'open google' in query:
            speak("Sir, please tell me what should i search in Google??") 
            search = takeCommand()
            speak("Searching...")
            kit.search(search)
            
            
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.get('chrome').open("youtube.com")
            
            
        elif 'play something' in query:
            speak("Sir, please say what should I play on YouTube?")
            play = takeCommand()
            speak("Playing on YouTube...")
            kit.playonyt(play)
            
            
        elif 'open facebook' in query:
            speak("Opening Facebook...")
            webbrowser.get('chrome').open("facebook.com")
            
            
        elif 'open instagram' in query:
            speak("Sir do you want me to open a specific user profile on Instagram?")
            condition1 = takeCommand()
            if 'yes' in condition1:
                speak("Sir, please enter the user name correctly below.")
                name = input("Enter the user name here:")
                speak("Opening the Instagram profile...")
                webbrowser.open(f"www.instagram.com/{name}")
                speak("Sir, would you like me to download the profile picture of this account?")
                condition2 = takeCommand()
                if 'yes' in condition2:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only = True)
                    speak("Task completed sir, profile picture is saved in main folder... Now i am good to go for your next command")
                else:
                    pass
            elif 'no' in condition1:
                speak("Opening your Instagram profile...")
                webbrowser.get('chrome').open("instagram.com")
            else:
                pass
            
            
        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow...")
            webbrowser.get('chrome').open("stackoverflow.com")
            
            
        elif 'open discord' in query:
            speak("Opening Discord, in a moment...")
            webbrowser.get('chrome').open("discord.com")       
            
            
        elif 'open spotify' in query:
            speak("Opening Spotify...")
            webbrowser.get('chrome').open("open.spotify.com")   
            
            
        elif 'open linkedin' in query:
            speak("Opening Linkedin...")
            webbrowser.get('chrome').open("linkedin.com")       
            
            
        elif 'open github' in query:
            speak("Opening GitHub...")
            webbrowser.get('chrome').open("github.com/sayan8662")
            
            
        elif 'open quora' in query:
            speak("Opening Quora...")
            webbrowser.get('chrome').open("quora.com")
            
            
        elif 'open code' in query:
            speak("Opening Code editor...Please be patient")
            code_path = "C:\\Users\\Sayan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
            
        elif 'close code' in query:
            speak("Okay sir...closing code editor")
            os.system("taskkill /f /im Code.exe")
            
            
        elif 'open game' in query:
            speak("Opening Valorant...Please wait")
            game_path = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(game_path)
            
            
        elif 'close game' in query:
            speak("Okay sir...closing Valorant")
            os.system("taskkill /f /im RiotClientServices.exe")
            
            
        elif 'close chrome' in query:
            speak("Okay sir...closing chrome")
            os.system("taskkill /f /im chrome.exe")
            
            
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke(language='en',category='all')
            speak(joke)
            
        
        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")
            
            
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
            
            
        elif 'sleep' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
            
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            
            
        elif 'open camera' in query:
            speak("Opening Camera...")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
            
        elif 'send an email' in query:  
                try:
                    speak("What should I sent?")
                    content = takeCommand()
                
                    if "send a file" in content:
                        email = 'sayankumarnandi@gmail.com'
                        password = 'Sayan2441139'
                        send_to = 'goutamkumarnandi66@gmail.com'
                        speak("Okay sir, what will be the subject for this email?")
                        subject = takeCommand()
                        speak("Now tell me the message for this email...")
                        message = takeCommand()
                        speak("Sir, please enter the correct path of the file into the shell")
                        file_location = input("Please enter the appropriate path here:")
                    
                        speak("Please be patient, I am sending the email now!")
                    
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = send_to
                        msg['Subject'] = subject
                    
                        msg.attach(MIMEText(message, 'plain'))
                    
                        filename = os.path.basename(file_location)
                        attachment = open(file_location, "rb")
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    
                        msg.attach(part)
                    
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        text = msg.as_string()
                        server.sendmail(email, send_to, text)
                        server.quit()
                        speak("Email hyas been sent to your father successfully.")
                
                    else:
                        email = 'sayankumarnandi@gmail.com'
                        password = 'Sayan2441139'
                        send_to = 'goutamkumarnandi66@gmail.com'
                        message = content
                    
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        server.sendmail(email, send_to, message)
                        server.quit()
                        speak("Email has been sent to your father successfully.")
                
                except Exception as e:
                    print(e)
                    speak("Unable to send the mail...Please try again.")
            
                
        elif 'remember' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("Sir, you want me to remember that " + data)
            remember = open('remember.txt','w')
            remember.write(data)
            remember.close()
            
            
        elif 'reminder for me' in query:
            remember = open('remember.txt','r')
            speak("you said me to remember the following: "+remember.read())
            
            
        elif 'ip address' in query:
            speak("Getting your IP address...")
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP address is {ip}")
            
            
        elif 'news' in query:
            speak("Please be patient sir, fetching latest news for you...")
            news()
            
            
        elif 'whatsapp to my mother' in query:
            speak("Sir...what message should i send to your Mother ?")
            message = takeCommand()
            kit.sendwhatmsg_instantly("+919477280246", message )
            speak("message sent..to your mother")
        
        
        elif 'whatsapp to my father' in query:
            speak("Sir...what message should i send to your Father ?")
            message = takeCommand()
            kit.sendwhatmsg_instantly("+919732907189", message )
        
        
        elif 'where i am' in query or 'where we are' in query:
            speak("Just a moment sir... Let me check it for you !!")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                location = geocoder.ip(ipAdd)
                speak(f"Sir I think we are in {location.city} city of state {location.state} in {pytz.country_names[location.country]}")
            
            except Exception as e:
                speak("Sorry sir... Due to some network issue I am unable to find where we are. Try it again after some time..")
                pass
        
        
        elif 'read a pdf' in query:
            pdf_read()
            
            
        elif "temperature" in query:
            ipAdd = requests.get('https://api.ipify.org').text
            location = geocoder.ip(ipAdd)
            search = f"temperature in {location.city}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            
            
        elif "activate how to do" in query:
            speak("HOW TO DO mode is activated now. Turning off this feature using voice command (like: 'exit' or 'close' ) is necessary when not in use. Now please tell me sir What HOW TO DO query you have?")
            while True:
                how = takeCommand()
                
                try:
                    if "exit" in how or "close" in how:
                        speak("Okay sir, HOW TO DO mode is deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                
                except Exception as e:
                    speak("I am SORRY sir, I am not aware of this procedure at the moment! Please try other")
                    
        
        elif "how much power left" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system has {percentage} percent battery left.")
            if percentage >= 75:
                speak("Enough power sir...we are good to go!")
            elif percentage >= 40 and percentage < 75:
                speak("Sir I think you should connect our system to the charging point for charging...")
            elif percentage >= 15 and percentage < 40:
                speak("Sir we don't have enough battery left, please connect our system to the charging point for charging...")
            else:
                speak("Sir we are running out of battery. Please connect our system to the charging point for charging or the system will shutdown very soon...")
                
        
        elif "weather" in query:
            own = pyowm.OWM('f654882faf68f2a87668b6f2c340e6f3')
            mgr = own.weather_manager()

            ipAdd = requests.get('https://api.ipify.org').text
            location = geocoder.ip(ipAdd)

            observation = mgr.weather_at_place(location.city)
            w = observation.weather

            temp = w.temperature('celsius')
            humidity = w.humidity
            status = w.detailed_status
            wind = w.wind()

            speak(f"Today's status is: {status}")
            for key,val in temp.items():
                speak(f'{key} is: {val} °C')
                
            speak(f'Humidity is: {humidity} %')
            
            for key,val in wind.items():
                speak(f'{key} is: {val}')
                
                
        elif 'no thanks' in query or 'no thank you' in query:
            speak("Okay sir...I am going to sleep now... Wake me Up whenever you need")
            break
        

        speak("Anything else you need, sir...?")
        
        
if __name__ == "__main__":
    
    while True:
        permission = takeCommand()
        
        if "wake up" in permission:
            TaskExecution()
            
        elif "bye" in permission:
            speak("Thank you sir! I am honoured to assist you with my all abilities. Have a great day...Going offline!")
            sys.exit()
    