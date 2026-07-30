"""
Speech module for Jarvis AI
Uses Microsoft Edge TTS + VLC for playback
"""

import asyncio
import os
import tempfile
import time

import edge_tts
import vlc

from config import ASSISTANT_NAME, VOICE


async def _generate_audio(text: str):
    communicate = edge_tts.Communicate(text, VOICE)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
        filename = temp.name

    await communicate.save(filename)
    return filename


def speak(text: str):
    print(f"{ASSISTANT_NAME}: {text}")

    filename = asyncio.run(_generate_audio(text))

    try:
        player = vlc.MediaPlayer(filename)

        player.play()

        # Give VLC time to start
        time.sleep(0.2)

        while player.is_playing():
            time.sleep(0.1)

        player.stop()

    finally:
        try:
            os.remove(filename)
        except PermissionError:
            # VLC may still have the file open for a brief moment
            time.sleep(0.5)
            if os.path.exists(filename):
                os.remove(filename)