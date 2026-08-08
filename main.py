from speech import speak
from utils.listener import listen
import time
from commands.web_commands import open_website
from commands.search_commands import google_search
from commands.youtube_commands import youtube_search
from commands.app_commands import open_application
from commands.system_commands import (
    battery_status,
    cpu_usage,
    ram_usage,
    disk_usage,
)
from commands.screenshot_commands import take_screenshot
from commands.volume_commands import volume_control
from commands.media_commands import media_control
from commands.time_commands import time_control , date_control
from commands.weather_commands import weather_control



def main():

    speak("Jarvis is ready.")

    while True:

        command = listen()

        if not command:
            continue

        if open_website(command):
           continue

        if google_search(command):
           continue

        if youtube_search(command):
           continue


        if open_application(command):
            continue

        if battery_status(command):
           continue

        if cpu_usage(command):
           continue

        if ram_usage(command):
           continue

        if disk_usage(command):
          continue

        if take_screenshot(command):
           continue

        if volume_control(command):
           continue

        if media_control(command):
           continue

        if time_control(command):
           continue

        if date_control(command):
           continue

        if weather_control(command):
           continue


        if command == "exit":
            speak("GoodBye.")
            break

        # Give the microphone a moment to fully release
        time.sleep(1)

        speak(f"You said {command}")


if __name__ == "__main__":
    main()