import speech_recognition as sr
import pyttsx3
import time

# Initialize recognizer and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the wake up call and response phrases
wake_up_call = "Hey Jarvis"
response_phrase = "Yes Sir"

def listen():
    """Listen for user input and return the text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text.lower()
        except Exception as e:
            print(f"Error: {e}")
            return ""

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def is_wake_up_call(text):
    """Check if the given text is the wake up call."""
    return text == wake_up_call

def main():
    """The main function that runs the voice assistant."""
    print("Voice Assistant is ready. Say 'Hey Jarvis' to activate.")
    while True:
        text = listen()
        if is_wake_up_call(text):
            speak(response_phrase)
            # Add your desired functionality here

if __name__ == "__main__":
    main()