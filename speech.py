"""
Speech module for Jarvis AI
Handles all text-to-speech functionality.
"""

import pyttsx3
from config import VOICE_RATE, VOICE_VOLUME, VOICE_ID

# Initialize engine
engine = pyttsx3.init()

# Apply configuration
engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)

voices = engine.getProperty("voices")
if voices and len(voices) > VOICE_ID:
    engine.setProperty("voice", voices[VOICE_ID].id)


def speak(text: str):
    """
    Speak the given text aloud.
    """

    try:
        print(f"Jarvis: {text}")
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Speech Error: {e}")


def stop():
    """
    Stop the speech engine.
    """
    engine.stop()