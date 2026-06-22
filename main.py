# Import libraries
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

# Create Speech Recognition object
recognizer = sr.Recognizer()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()


# Function to make Jarvis speak
def speak(text):
    engine.say(text)          # Convert text to speech
    engine.runAndWait()       # Wait until speaking is complete


# Function to process user commands
def processcommand(command):

    # Convert command to lowercase
    command = command.lower()

    # Open Google
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Open ChatGPT
    elif "open chatgpt" in command:
        speak("Opening Chat GPT")
        webbrowser.open("https://chatgpt.com")

    # Play Music
    elif command.startswith("play"):

        # Extract song name
        song = command.replace("play", "").strip()

        # Check if song exists in library
        if song in musiclibrary.music:
            link = musiclibrary.music[song]

            speak(f"Playing {song}")
            webbrowser.open(link)

        else:
            speak("Song not found in library")


# Main Program
if __name__ == "__main__":

    # Startup message
    speak("Initializing Jarvis")

    # Infinite loop
    while True:

        print("Recognizing...")

        try:

            # Listen for wake word
            with sr.Microphone() as source:

                print("Listening...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            # Convert speech to text
            word = recognizer.recognize_google(audio)

            # Check wake word
            if word.lower() == "jarvis":

                speak("Yes, I am listening")

                # Listen for actual command
                with sr.Microphone() as source:

                    print("Waiting for command...")

                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                # Convert command speech to text
                command = recognizer.recognize_google(audio)

                print("Command:", command)

                # Execute command
                processcommand(command)

        # Handle errors
        except Exception as e:
            print("Error:", e)

# Run  python main.py