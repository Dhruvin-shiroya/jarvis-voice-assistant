import speech_recognition as sr
import webbrowser 
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(command):
    command = command.lower()

# Process user commands

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open chatgpt" in command:
        speak("Opening Chat GPT")
        webbrowser.open("https://chatgpt.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)


# Main program
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        r = sr.Recognizer()
        print("recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit= 5
                )

            word = recognizer.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes,I am listening")

                with sr.Microphone() as source:
                    print("Waiting for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
        
                    processcommand(command)

        except Exception as e:
            print("Error:", e)




# Run python main.py
