import time
from win32com.client import Dispatch

def speak(str):
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

a=1
b=2
while a<b:
    speak("Drink water sir")
    time.sleep(60*30)
    speak("do eye exercise")
    time.sleep(60*60)
    speak("do physical activity")