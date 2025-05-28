import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time

# Initializing the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def get_query(x):
    """Defining a function to get users command """

    print("Your command: ")
    engine.say("Your command!")
    engine.runAndWait()
    """using the recognizer function to convert the spoken command into text"""

    audio = recognizer.listen(x)
    y = recognizer.recognize_google(audio)
    y = y.lower()
    return y

commands = {
    "who are you" : lambda: "I am your friend RoboSpeaker 1.301",
    "who made you" : lambda: "I was made by Kartik",
    "what is the time" : lambda: time.strftime("%H %M"),
    "what is the date today" : lambda: datetime.date.today(),
    "who is the president of usa" : lambda: "The president of usa is Donald Duck",
    "open google" : lambda: "opening google.com",
    "open youtube" : lambda: "opening youtube.com",
}
while True:
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            query = get_query(source)
            if query in commands:
                if query == "open google" or query == "open youtube":
                    response = commands[query]()
                    webbrowser.open(f"{query[4:]}.com")
                else:
                    response = commands[query]()
                print(response)
                engine.say(response)
                engine.runAndWait()
            elif "bye" in query:
                print("Goodbye and have a nice day!")
                engine.say("Goodbye and have a nice day!")
                engine.runAndWait()
                break
            else:
                print("Sorry, I didn't understand.")
                engine.say("Sorry, I didn't understand.")
                engine.runAndWait()
                continue
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        engine.say("Google Speech Recognition could not understand audio")
        engine.runAndWait()
        break

    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service!, check your internet connection")
        engine.say("Could not request results from Google Speech Recognition service!, check your internet connection")
        engine.runAndWait()
        break

    except KeyboardInterrupt:
        print("Bye Have a good day")
        engine.say("Bye Have a good day")
        engine.runAndWait()
        break

    except Exception as e:
        print(e)
        break