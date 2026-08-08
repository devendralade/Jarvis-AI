from datetime import datetime
from speech import speak


def time_control(command):
    command = command.lower()

    time_keywords = [
        "what time is it",
        "current time",
        "time now",
        "tell me the time"
    ]

    if any(keyword in command for keyword in time_keywords):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%I:%M %p")

        speak(f"The current time is {formatted_time}")

        return True
 
    return False

def date_control(command):
    command = command.lower()

    date_keywords = [
        "what is today's date",
        "what date is it",
        "today's date",
        "tell me the date",
        "current date"
    ]

    if any(keyword in command for keyword in date_keywords):
        current_date = datetime.now()
        formatted_date = current_date.strftime("%B %d, %Y")

        speak(f"The date today is {formatted_date}")

        return True
 
    return False
