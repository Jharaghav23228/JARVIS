import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
from openai import OpenAI
recognizer=sr.Recognizer()
engine=pyttsx3.init()
api="0f9ba675f17840d1b8ab3e0ba074c6d7"

def speak(text):
    engine.say(text)
    engine.runAndWait() 
    
def aiprocess(command):
    client=OpenAI(api_key="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",)    
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis ."},
        {
            "role": "user",
            "content": command
        }
    ]
)

    return completion.choices[0].message.content
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower(). startswith("play"):
        song=c.lower().split(" ")[1] 
        link=MusicLibrary.music[song]
        webbrowser.open(link)
    elif "headline" in c.lower():
       r=requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api}")          
       if r.status_code==200:
           data =r.json()
           articles=data.get("articles",[])
           
           for article in articles:
               speak(article["title"]) 
    
    else:
        output=aiprocess(c)
        speak(output)
    
if __name__=="__main__":
    speak("Initializing Jarvis.....")
    while True:
        r= sr.Recognizer()
           
        print("Recognizing......")    
        try:
            with sr.Microphone() as source:
              print("Listening......!")
              audio=r.listen(source, timeout=2,phrase_time_limit=2)
            word= r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Hello Raghav")
            
                with sr.Microphone() as source:
                  print("Jarvis Activated......!")
                  audio=r.listen(source)
                  command=r.recognize_google(audio)
                  processCommand(command) 
                 
        except Exception as e:
            print("Error".format(e))            
            
            