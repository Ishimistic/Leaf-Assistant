# 🌿 Leaf Assistant

**Leaf Assistant** is a voice-controlled personal assistant built using Python. It can listen to your voice commands and perform tasks like:

- Speaking answers using Google Text-to-Speech
- Searching for meanings and information
- Playing YouTube songs
- Opening websites
- Gracefully stopping speech or shutting down the assistant



## 🧠 Features

- 🎤 Voice command recognition using `speech_recognition`
- 🔊 Speech response using `gTTS` + `playsound`
- 📚 Wikipedia search
- 🔍 Google meaning lookup
- ▶️ YouTube search and playback
- 🌐 Opens websites like Google, YouTube, LinkedIn
- 🔁 Graceful interrupt with `Ctrl + C`
- 🛑 Stop speech instantly by saying `"stop"`



## 📦 Tech Stack

- Python 3.10+
- `speech_recognition`
- `gTTS`
- `playsound`
- `wikipedia`
- `pywhatkit`
- `requests`, `BeautifulSoup`



## 🛠️ Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/leaf-assistant.git
   cd leaf-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. For microphone input, make sure you have PyAudio:
   ```bash
   pipwin install pyaudio
   ```

##  Usage
```bash
python assistant.py
```
Once the assistant starts, you can try saying:
- "play despacito"
- "meaning of serendipity"
- "tell me about Python"
- "open YouTube"
- "exit" or press Ctrl + C to quit

## 📁 Project Structure
```bash
leaf-assistant/
│
├── assistant.py          # Main file
├── core/
│   ├── listen.py         # Handles listening logic
│   └── speak.py          # Handles speaking (TTS) logic
|   |_ action.py
├── requirements.txt
└── README.md

```

