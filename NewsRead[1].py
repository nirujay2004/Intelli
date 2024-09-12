import eel
import requests
import json
import pyttsx3
from command import takecommand

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    # eel.DisplayMessage(text)
    engine.say(text)
    # eel.receiverText(text)
    engine.runAndWait()
@eel.expose
def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1646c6e9f0dd48209586f0673c022157",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=1646c6e9f0dd48209586f0673c022157",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=1646c6e9f0dd48209586f0673c022157",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=1646c6e9f0dd48209586f0673c022157",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=1646c6e9f0dd48209586f0673c022157",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=1646c6e9f0dd48209586f0673c022157"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    # field = input("Type field news that you want: ")
    query = takecommand()
    for key ,value in api_dict.items():
        if key.lower() in query.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the news.")

    arts = news["articles"]
    counter = 0

    for articles in arts :
        article = articles["title"]
        print(article)
        eel.DisplayMessage(article)
        speak(article)
        counter += 1
        if counter == 3:
            break
        
    # for articles in arts :
    #     article = articles["title"]
    #     print(article)
    #     eel.DisplayMessage(article)
    #     speak(article)
    #     pass
      
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        
        # a = input("[press 1 to continue] and [press 2 to stop]")
        # if str(a) == "1":
        #     pass
        # elif str(a) == "2":
        #    break
        #     # pass
        speak("here is the another one")
        eel.DisplayMessage("here is the another one")
        
    eel.DisplayMessage("that's all")
    speak("that's all")
    eel.ShowHood()
   
latestnews()  