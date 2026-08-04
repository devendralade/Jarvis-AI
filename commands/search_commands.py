import webbrowser
import urllib.parse

from speech import speak


def google_search(command):
    command = command.lower().strip()

    if not command.startswith("search"):
        return False

    query = command.replace("search", "", 1).strip()

    if not query:
        speak("What would you like me to search?")
        return True

    speak(f"Searching Google for {query}")

    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

    webbrowser.open(url)

    return True