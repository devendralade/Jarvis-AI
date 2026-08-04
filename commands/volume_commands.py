import pyautogui

from speech import speak


def volume_control(command):

    command = command.lower()

    # ----------------- MUTE -----------------

    if "mute" in command:

        pyautogui.press("volumemute")

        speak("Volume muted.")

        return True

    # ----------------- INCREASE -----------------

    if "increase volume" in command or "volume up" in command:

        speak("Increasing volume.")

        for _ in range(5):
            pyautogui.press("volumeup")

        return True

    # ----------------- DECREASE -----------------

    if "decrease volume" in command or "volume down" in command:

        speak("Decreasing volume.")

        for _ in range(5):
            pyautogui.press("volumedown")

        return True

    return False