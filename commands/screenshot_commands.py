import os
from datetime import datetime
import pyautogui

from speech import speak


def take_screenshot(command):

    command = command.lower()

    keywords = [
        "screenshot",
        "take screenshot",
        "capture screen",
        "screen capture",
    ]

    if not any(word in command for word in keywords):
        return False

    try:
        folder = "Screenshots"
        os.makedirs(folder, exist_ok=True)

        filename = datetime.now().strftime(
            "Screenshot_%Y-%m-%d_%H-%M-%S.png"
        )

        path = os.path.join(folder, filename)

        speak("Taking screenshot.")

        image = pyautogui.screenshot()
        image.save(path)

        speak("Screenshot saved successfully.")

    except Exception as e:
        print(e)
        speak("Sorry, I couldn't take the screenshot.")

    return True