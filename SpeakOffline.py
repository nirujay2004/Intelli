#pip install pyttsx3
import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate', 150)
engine.setProperty('voice', voices[1].id)


def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
    print(Fore.CYAN+audio)
    engine.say(audio)
    engine.runAndWait()
Speak("Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy. IBM has a rich history with machine learning.")