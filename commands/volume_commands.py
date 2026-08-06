import pyautogui

from speech import speak


def volume_control(command):
    command = command.lower()
    words = command.split()

    if "mute" in command:
        pyautogui.press("volumemute")
        speak("Muting volume")

        return True 

    increase_keywords = [
    "increase volume by",
    "volume up by ",
    "turn up the volume by",
]

    if any(keyword in command for keyword in increase_keywords):
        

        try:
            amount = int(words[-1])
            speak(f"Increasing volume by {amount}")
            pyautogui.press("volumeup", presses=amount//2)
        except ValueError:
            speak("Please say something like 'increase volume by 10'.")

       
          
        return True

    decrease_keywords = [
        "decrease volume by",
        "volume down by ",
        "turn down the volume by "
    ]

    if any(keyword in command for keyword in decrease_keywords):
        
        try:
            amount = int(words[-1])
            speak(f"Decreasing volume by {amount}")
            pyautogui.press("volumedown", presses=amount//2)
        except ValueError:
            speak("plase say something like 'decrease volume by 10' ")
        
            
        return True

    return False







