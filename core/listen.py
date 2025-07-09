import speech_recognition as sr
from core.speak import speak

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1.2
        recognizer.energy_threshold = 300
        # audio = recognizer.listen(source)
       
        try:
           recognizer.adjust_for_ambient_noise(source, duration=1)
           audio = recognizer.listen(source, timeout = 10, phrase_time_limit=15)
        # print("Your query: " + query)
        # return query

        except sr.WaitTimeoutError:
           print("No speech detected within the time window.")
           speak("I didn't hear anything. Please try again.")
           return ""
        
    try:
        query = recognizer.recognize_google(audio).lower()
        print("Your query: " + query)
        return query
    except:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return ""
