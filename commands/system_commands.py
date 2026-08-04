import psutil
from speech import speak

# this will tell use the cpu usage 
def cpu_usage(command):

    command = command.lower()

    if "cpu" not in command:
        return False

    usage = psutil.cpu_percent(interval=1)

    speak(f"CPU usage is currently {usage} percent.")

    return True


# to check the ram usage 
def ram_usage(command):

    command = command.lower()

    keywords = [
        "ram",
        "memory"
    ]

    if not any(word in command for word in keywords):
        return False

    memory = psutil.virtual_memory()

    used = round(memory.used / (1024 ** 3), 2)
    total = round(memory.total / (1024 ** 3), 2)

    speak(
        f"RAM usage is {memory.percent} percent. "
        f"{used} GB used out of {total} GB."
    )

    return True

# to check disk usage 
def disk_usage(command):

    command = command.lower()

    if "disk" not in command:
        return False

    disk = psutil.disk_usage("C:\\")

    used = round(disk.used / (1024 ** 3), 2)
    total = round(disk.total / (1024 ** 3), 2)

    speak(
        f"Drive C is {disk.percent} percent full. "
        f"{used} GB used out of {total} GB."
    )

    return True

# to chek the battery
def battery_status(command):
    command = command.lower()

    battery_keywords = [
        "battery",
        "battery percentage",
        "battery status",
        "charge"
    ]

    if not any(keyword in command for keyword in battery_keywords):
        return False

    battery = psutil.sensors_battery()

    if battery is None:
        speak("Sorry, I couldn't detect a battery on this device.")
        return True

    percent = battery.percent

   

    if percent >= 90:
      status = "Battery level is excellent."

    elif percent >= 60:
      status = "Battery level is good."

    elif percent >= 30:
      status = "Battery is getting low."

    else:
     status = "Battery is critically low. Please connect the charger."

    if battery.power_plugged:
        speak(f"Your battery is {percent} percent and it is charging.")
    else:
            speak(f"Your battery is {percent} percent. {status}")

    return True