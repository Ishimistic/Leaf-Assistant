from core.speak import speak, stop_signal
from core.listen import listen
from core.actions import (
    get_meaning_from_google,
    play_on_youtube,
    tell_me_about,
    open_target
)

def main():
    try: 
        speak("Hello, I am Leaf Assistant. How can I help you today?")
        while True:
            command = listen()
            if command == "":
                continue

            elif "what sound does" in command:
                animal = command.replace("what sound does", "").replace("make", "").strip()
                speak(f"The sound of {animal} is usually a 'sound'.")

            elif any(word in command for word in ["play", "song", "music"]):
                song = command.replace("play", "").replace("song", "").strip()
                play_on_youtube(song)

            elif "tell me " in command or "what is " in command or "meaning " in command or "something " in command:
                topic = command.replace("tell me ", "").replace("what is", "").replace("meaning of", "").strip()
                tell_me_about(topic)

            elif "open" in command:
                open_target(command)

            elif "stop" in command:
                stop_signal.set()
                print("[INFO] Speech stopped by user.")
                continue

            elif "exit" in command or "quit" in command:
                speak("Goodbye! Have a great day!")
                break

            else:
                speak("Sorry, I didn't understand that command. Please try again.")
                break

    except KeyboardInterrupt:
        print("\n[INFO] Exiting on keyboard interrupt...")
        speak("Goodbye! Assistant is shutting down.")

if __name__ == "__main__":
    main()
