import webbrowser
from speech import speak

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.in",
    "stackoverflow": "https://stackoverflow.com"
}

def open_website(command):
    command = command.lower()

    for website, url in WEBSITES.items():
        if website in command:
            speak(f"Opening {website}")
            webbrowser.open(url)
            return True

    return False