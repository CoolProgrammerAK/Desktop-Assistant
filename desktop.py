import requests
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import os
import subprocess
import smtplib
import winshell
import random
import time
import ctypes
import cv2
import pyjokes
import datetime
from selenium import webdriver


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour
    if(hour < 12):
        speak("Good Morning Sir")

    elif(hour >= 12 and hour < 17):
        speak("Good Afternoon sir")
    else:
        speak("Good Evening Sir")
    speak("I am Aleeza. How may can I help you??")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.energy_threshold=300
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        text = r.recognize_google(audio, language="en-in")
        print(text)
    except Exception as e:
        print("Unable to Recognize your voice.")
        print("Say that again please")
        return "None"
    return text


def playsong():
    music_dir = "C:\\Users\\HP\\Music"
    songs = os.listdir(music_dir)
    speak("Here is the list of songs available")
    lens = len(songs)
    no = 1
    for i in songs:

        print(f"{no}. {i}")
        no = no+1
    speak("Tell me which song you want to hear?")

    awaitedsong = takecommand()
    playsong = ""
    try:
        for song in songs:
            if str(awaitedsong).lower() in song.lower():
                speak("Here you go with the music of your choice")
                playsong = song

                os.startfile(os.path.join(music_dir, playsong))

        if(playsong == ""):
            speak("Sir as we did not get your choice so we will play music according to our own chioce. Hope you will enjoy ")
            s = random.randint(1, lens-1)
            speak("Here you go with music")
            os.startfile(os.path.join(music_dir, songs[s]))

    except Exception as e:

        print(e)
        speak("Sorry sir, I am not able to play music at the moment. Hope you understand")


def playmovie():
    movie_dir = "D:\\movies"
    movies = os.listdir(movie_dir)
    speak("Here is the list of movies available")
    lens = len(movies)
    no = 1
    for i in movies:

        print(f"{no}. {i}")
        no = no+1
    speak("Tell me which movie you want to watch?")

    awaitedmovie = takecommand()
    playmovie = ""
    try:
        for movie in movies:
            if str(awaitedmovie).lower() in movie.lower():
                speak("Here you go with the movie of your choice")
                playmovie = movie

                os.startfile(os.path.join(movie_dir, playmovie))

        if(playmovie == ""):
            speak("Sir as we did not get your choice so we will play movie according to our own chioce. Hope you will enjoy ")
            s = random.randint(1, lens-1)
            speak("Here you go with movie of your choice")
            os.startfile(os.path.join(movie_dir, movies[s]))

    except Exception as e:

        print(e)
        speak("Sorry sir, I am not able to play movie at the moment. Hope you understand")


def open_application(query):
    if "youtube" in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
        return

    elif "instagram" in query:
        speak("Here you go to Instagram\n")
        webbrowser.open("instagram.com")
        return

    elif "google" in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")
        return

    elif "stackoverflow" in query or "stack overflow" in query:
        speak("Here you go to Stackoverflow\n")
        webbrowser.open("stackoverflow.com")
        return
    elif "wikipedia" in query:
        speak("Here you go to Wikipedia\n")
        webbrowser.open("wikipedia.com")
        return
    elif "visual studio code" in query:
        speak("Here you go to Visual Studio Code\n")
        code = "C:\\Users\\HARISH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code)
        return
    elif "excel" in query:
        speak("Here you go to Microsoft Excel\n")
        code = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk"
        os.startfile(code)
        return
    elif "office" in query:
        speak("Here you go to Microsoft Office\n")
        code = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"
        os.startfile(code)
        return
    elif "powerpoint" in query:
        speak("Here you go to Microsoft PowerPoint\n")
        code = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk"
        os.startfile(code)
        return
    elif "chrome" in query:
        speak("Here you go to Google Chrome\n")
        code = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(code)
        return
    elif "firefox" in query or "mozilla" in query:
        speak("Here you go to Mozilla Firefox\n")
        code = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
        os.startfile(code)
        return
    else:

        speak("Sorry sir,Application not available")
        return


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("avineykhetarpal01@gmail.com", "kantarani")
    server.sendmail("avineykhetarpal01@gmail.com", to, content)
    server.close()


def day():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]

        speak("Sir,The day is " + day_of_the_week)


def month():
    strmonth = datetime.datetime.now().month
    month_dict = {1: 'January', 2: 'February',
                  3: 'March', 4: 'April',
                  5: 'May', 6: 'June',
                  7: 'July', 8: 'August', 10: 'October',
                  9: 'September', 11: 'November',
                  12: 'December'}
    if strmonth in month_dict.keys():
        speak("Sir,The month is " + month_dict[strmonth])


def choice():
    speak("Sir,Tell me your next query")


def Convert(string):
    li = list(string.split(" "))
    return li


def search_input(query):
    driver = webdriver.Chrome("C:\\chromedriver.exe")
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in query:

        speak("Opening in youtube")
        data = ["search", "in", "youtube", "play"]
        for item in data:
            query = query.replace(item, "")
        data2 = []
        data2 = Convert(query)
        print(data2)
        for item in data2:
            if(item) == '':
                data2.remove(item)

        driver.get(
            "http://www.youtube.com/results?search_query=" + '+'.join(data2))
        choice()
        return

    elif 'wikipedia' in query.lower():

        speak("Opening wikipedia")
        data = ["search", "in", "wikipedia", "play"]
        for item in data:
            query = query.replace(item, "")
        data2 = []
        data2 = Convert(query)
        print(data2)
        for item in data2:
            if(item) == '':
                data2.remove(item)

        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(data2))
        choice()
        return
    else:
        speak("Opening Google")
        data = ["search", "in", "google", "play"]
        for item in data:
            query = query.replace(item, "")
        data2 = []
        data2 = Convert(query)

        for item in data2:
            if(item) == '':
                data2.remove(item)
        driver.get("https://www.google.com/search?q=" + '+'.join(data2))
        choice()
        return


def process_text(query):
    try:
        if "open" in query:
            open_application(query)
            choice()
            return

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"Sir,the time is {strtime}")
            choice()
            return
        elif "day" in query and "birthday" not in query:
            day()
            choice()
            return
        elif "month" in query:
            month()
            choice()
            return
        elif "year" in query:
            strday = datetime.datetime.now().year
            speak(f"Sir,the year is {strday}")
            choice()
            return

        elif 'music' in query or "songs" in query or "song" in query:

            playsong()
            choice()
            return

        elif "movie" in query or "movies" in query:

            playmovie()
            speak("Sir,Tell me your next query")
            return
        elif "name" in query:
            speak("I am Aleeza. Your desktop Assistant")
            choice()
            return
        elif "who are you" in query or "yourself" in query:
            speakd = '''Hello, I am Person. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            speak(speakd)
            choice()
            return

        elif "who made you" in query or "created you" in query:
            speakd = "I have been created by Aviney Sir."
            speak(speakd)
            choice()
            return

        elif "send email" in query:
            try:
                speak("What should you want to say")
                content = takecommand()
                if(content != "None"):
                    speak("whom should i send.Enter in terminal")
                    to = input("Enter email address\n")
                    sendEmail(to, content)
                    speak("Email Sent successfully")
                else:
                    speak("Cannot able to judge what you are saying. So try again.")

                choice()

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")
                choice()
            return

        elif "gf" in query or "bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            choice()
            return
        elif "calculate" in query:
            app_id = "K774XR-ELGY95LE8W"
            client = wolframalpha.Client(app_id)

            indx = query.lower().split().index('calculate')
            query2 = query.split()[indx + 1:]
            res = client.query(' '.join(query2))
            answer = next(res.results).text
            speak("The answer is " + answer)
            print(answer)
            choice()
            return
        elif 'search' in query or 'play' in query:
            # a basic web crawler using selenium
            search_input(query)
            return
        elif 'love' in query:
            speak("It is 7th sense that destroy all other senses")
            choice()
        elif "change background" in query:
            ctypes.windll.user32.SystemParametersInfoA(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
            choice()
            return
        elif "joke" in query:
            speak("Here's the joke")
            speak(pyjokes.get_joke())
            speak("Hope u enjoyed it")
            choice()
            return
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            choice()
            return
        elif "shutdown" in query:
            speak("Are you sure you want to shutdown your computer?")
            ans = takecommand().lower()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                speak("Switching off your computer")
                os.system("shutdown /s")
            else:
                choice()
                return
        elif "hibernate" in query or "sleep" in query:
            speak("Are you sure you want to hibernate your computer?")
            ans = takecommand().lower()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                speak("Hibernating")
                os.system("shutdown /h")
            else:
                choice()
                return
        elif "restart" in query:
            speak("Are you sure you want to restart your computer?")
            ans = takecommand().lower()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                speak("Restarting")
                os.system("shutdown /r")
            else:
                choice()
                return

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
            speak("Recycle Bin Recycled")
            choice()
            return

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Just wait for a moment")
           
            webbrowser.open(
                "https://www.google.nl/maps/place/" + location + "")
            choice()
            return

        elif "camera" in query or "take a photo" in query:
            camera=cv2.VideoCapture(0,cv2.CAP_DSHOW)
            ret,frame = camera.read()
            while(True):
                cv2.imshow('img',frame)
                speak("Would you like to save this photo?")
                ans = takecommand().lower()

                if 'yes' in str(ans) or 'yeah' in str(ans):
                  
                  cv2.imwrite('c1.png',frame)
                  cv2.destroyAllWindows()
                  
                  break
                else:
                    speak("As we didn't get the required output to save this photo,so we will deleting this photo")
                    cv2.destroyAllWindows()
                    break

                
            
            camera.release()
            choice()
            return

        elif 'news' in query:
            try:
                 data=requests.get("https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=01ac17cb0ef940cb83d7e2d67f322844").json()
                 speak('Here are some top news from the times of india')
                 print('''=============== TIMES OF INDIA ============'''+ '\n')
                 i=1
                 for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

                 speak("That's All")
                 choice()
                 return
            except Exception as e:
                 speak("Sorry,we could not complete your request at moment")

                 choice()
                 return
           
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "7862efd0c20c59a8764fe9c37b4d39e3"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("What is the City name ")
            city_name = takecommand().lower()
            print(city_name)
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" Sir,City Not Found ")
            choice()
            return

    
        else:

            speak("I can search the web for you, Do you want to continue?")
            ans = takecommand()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_input(ans.lower())
            else:
                speak("Ok,Then tell me another query?")
                return
    except Exception:

        speak("I don't understand, I can search the web for you, Do you want to continue?")
        ans = takecommand()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_input(ans.lower())
        else:
            speak("Ok,Then tell me another query?")
            return


if __name__ == '__main__':
    wishme()
    while(True):
        query = takecommand().lower()
     
        if(query == "none"):
            speak("Sir,Please speak something")
            continue
        elif "exit" in str(query) or "bye" in str(query)  or "quit" in str(query):
            speak("Ok bye,sir")
            break
        
       
        process_text(query)
            

      
