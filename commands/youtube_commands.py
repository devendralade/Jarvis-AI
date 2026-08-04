import webbrowser
import urllib.parse

from speech import speak


def youtube_search(command):
    command = command.lower().strip()

    if not command.startswith("play"):
        return False

    query = command.replace("play", "", 1).strip()

    if not query:
        speak("What would you like me to play?")
        return True

    speak(f"Playing {query} on YouTube")

    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return True