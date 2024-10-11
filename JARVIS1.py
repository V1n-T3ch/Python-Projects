import speech_recognition as sr
import pyttsx3
import webbrowser
from colorama import Fore, Style
import platform, os

OsName = platform.uname()[0]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        query = ""
    except sr.RequestError as e:
        print("Sorry, I couldn't request results; {0}".format(e))
        query = ""
    return query

def open_website(url):
    webbrowser.open(url)

def banner():
        if OsName == "Windows":
            os.system("cls")
        else:
            os.system("clear")
            print(Fore.LIGHTWHITE_EX + " ██╗    ██╗██╗  ██╗██╗██████╗ ███████╗    ██████╗  ██████╗ ████████╗")
            print(Fore.LIGHTWHITE_EX + " ██║    ██║██║  ██║██║██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝")
            print(Fore.LIGHTWHITE_EX + " ██║ █╗ ██║███████║██║██████╔╝███████╗    ██████╔╝██║   ██║   ██║   ")
            print(Fore.LIGHTWHITE_EX + " ██║███╗██║██╔══██║██║██╔══██╗╚════██║    ██╔══██╗██║   ██║   ██║   ")
            print(Fore.LIGHTWHITE_EX + " ╚███╔███╔╝██║  ██║██║██║  ██║███████║    ██████╔╝╚██████╔╝   ██║   ")
            print(Fore.LIGHTWHITE_EX + "  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ")
            print(Style.RESET_ALL)
banner()
def main():
    while True:
        wakeup_call = "hey jarvis"
        print("Waiting for wakeup call...")
        query = listen()
        if query == wakeup_call:
            print("Yes sir")
            speak("Yes sir")
            speak("What can I do for you, sir?")
            action = listen()
            if "open browser" in action:
                speak("Sure sir, opening browser.")
                open_website("https://www.google.com")  # Change the URL as per your requirement
            elif "open" in action and "website" in action:
                speak("Please specify the website URL.")
                website_url = listen()
                speak(f"Opening {website_url}")
                open_website(website_url)
            elif "exit" in action or "quit" in action:
                speak("Goodbye sir.")
                break
            else:
                speak("Sorry sir, I didn't understand your command.")

if __name__ == "__main__":
    main()
