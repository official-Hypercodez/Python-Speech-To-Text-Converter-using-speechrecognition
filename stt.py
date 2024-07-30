import speech_recognition as sr

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.adjust_for_ambient_noise(source)
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query=r.recognize_google(audio)
		print(f"You Said : {query}")
	except Exception as e:
		print("Say that again please.")
		return "None"
	return query

if __name__ == "__main__":
	takeCommand()