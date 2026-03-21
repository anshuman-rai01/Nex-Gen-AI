from datetime import datetime
import webbrowser
import requests

import speech_recognition as sr
import pyttsx3
import pyaudio
engine = pyttsx3.init()
engine.setProperty('rate',170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
    try:
        query = rec.recognize_google(audio)
        print("You : ", query)
        return query.lower()
    except:
        print("Can't understand you, please say that again...")
        return ""

greet_msgs = ["hi","hello","hey","hi there","hello there"]
date_msgs = ["date","tell me date","today's date"]
time_msgs = ["time","tell me time","today's time"]
news_msgs = ["news","tell me news","headlines"] 
weather_msgs = ["weather","today weather","current weather"]

def get_news():
  api_key = "d95b49ace30fddbeeec6a4c399e90654"
  url = f"https://api.openweathermap.org/data/2.5/weather?lat=28.6327&lon=77.2198&appid={api_key}"
  response = requests.get(url)
  data = response.json()
  articles = data["articles"][:5]
  for i in range(len(articles)):
    print(articles[i]["title"])
chat = True
while chat:
  # user_msg = input("Enter your message : ").lower()
  user_msg = listen()
  if user_msg in  greet_msgs:
    speak("Hello user. How may I help you . ")
  elif user_msg in date_msgs:
    speak(f"Today's date is :{datetime.now().date()}")
  elif user_msg in time_msgs:
    current_time = datetime.now().time()
    print(f"Time is :{current_time.strftime('%I:%M:%S %p')}")
  elif "open" in user_msg:
    website_name = user_msg.split()[-1]
    webbrowser.open(f"https://www.{website_name}.com")
  elif "calculate" in user_msg:
    expression = user_msg.split()[-1]
    result = eval(expression)
    print("Result is : ", result)
  elif user_msg in news_msgs:
    get_news()
  elif user_msg=="bye" :
    chat = False
  else:
    speak("I cannot understand ")