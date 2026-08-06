import pyautogui

from speech import speak

def media_control(command):
    command = command.lower() 

    play_pause_keywords = [
        "play or pause",
        "resume",
        "pause" ,
        "continue"
        
    ]

    if any(keyword in command for keyword in play_pause_keywords):

        if "pause" in command:
          speak("Pausing media.")

        elif "resume" in command or "continue" in command:
          speak("Resuming media.")

        else:
         speak("Toggling playback.")
        
        pyautogui.press("playpause")

        return True

    next_keywords = [
    "next song",
    "next track",
    "skip song"
]

    if any(keyword in command for keyword in next_keywords):
        speak("palying the next track ")
        pyautogui.press("nexttrack")

        return True

    prev_keywords= [
        "previous song",
        "previous track",
        "erlier song"
    ]

    if any(keyword in command for keyword in prev_keywords):
        speak("playing the previous track ")
        pyautogui.press("prevtrack")

        return True


    return False



