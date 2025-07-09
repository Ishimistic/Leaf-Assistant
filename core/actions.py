import requests
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
import webbrowser
from core.speak import speak

def get_meaning_from_google(term):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q=meaning+of+{term}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    meaning = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

    if meaning:
        text = meaning.get_text()
        speak(f"The meaning of {term} is: {text}")
    else:
        speak("Sorry, I couldn't find the meaning of that term.")

def play_on_youtube(query):
    speak(f"Playing {query} on YouTube.")
    pywhatkit.playonyt(query)

def tell_me_about(query):
    try:
        summary = wikipedia.summary(query, sentences=4)
        speak(summary)
    except:
        speak("Sorry, I couldn't find any information on that topic.")

    google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    speak(f"You can also check Google for more information on {query}. And if something else then let me know")
    webbrowser.open(google_url)

def open_target(query):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "linkedin": "https://www.linkedin.com",
    }

    for name in websites:
        if name in query:
            speak(f"Opening {name}.")
            webbrowser.open(websites[name])
            return

    speak("Sorry, I didn't recognize the website you wanted to open.")
