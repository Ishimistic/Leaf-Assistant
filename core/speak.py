from gtts import gTTS
from playsound import playsound
import tempfile
import os
import threading
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

stop_signal = threading.Event()

def speak(text):
    print("Assistant:", text)
    stop_signal.clear()

    def _speak():
        try:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            temp_path = temp_file.name
            temp_file.close()

            tts = gTTS(text=text, lang="en")
            tts.save(temp_path)

            if not stop_signal.is_set():
                playsound(temp_path)

            os.remove(temp_path)

        except Exception as e:
            print(f"[TTS ERROR] Could not speak. Error: {e}")

    t = threading.Thread(target=_speak)
    t.start()
    # try:
    #     t.join()
    # except KeyboardInterrupt:
    #     stop_signal.set()
    #     print("\n[INFO] Ctrl + C detected. Speech interrupted.")
    #     # Exit immediately if desired:
    #     sys.exit(0)
    t.join()
