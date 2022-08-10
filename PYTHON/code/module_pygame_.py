def speak(str):
    from win32com.client import Dispatch
    s=Dispatch("SAPI.Spvoice")
    s.Speak(str)

speak("you are my boss")