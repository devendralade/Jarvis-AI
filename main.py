from speech import speak
from utils.listener import listen
import time


def main():

    speak("Jarvis is ready.")

    while True:

        command = listen()

        if not command:
            continue

        if command == "exit":
            speak("Goodbye.")
            break

        # Give the microphone a moment to fully release
        time.sleep(1)

        speak(f"You said {command}")


if __name__ == "__main__":
    main()