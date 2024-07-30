Speech Recognition Command Listener
This Python script listens to audio input from the microphone and uses Google's Speech Recognition API to convert the spoken words into text.

Requirements
Python 3.x
speech_recognition library
You can install the necessary libraries using:
 pip install speechrecognition
Usage
Run the script to start listening for audio input and recognizing speech:

python stt.py
The script will print out the recognized text from the audio input.

Code Overview
python
Copy code
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You Said: {query}")
    except Exception as e:
        print("Say that again please.")
        return "None"
    return query

if __name__ == "__main__":
    takeCommand()
takeCommand function: Initializes the recognizer and microphone, listens for audio input, and attempts to recognize the speech using Google's Speech Recognition API.
Exception Handling: If the recognition fails, it will prompt the user to speak again.
