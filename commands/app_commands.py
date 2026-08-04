import subprocess

from speech import speak


APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "command prompt": "cmd",
    "cmd": "cmd",
    "file explorer": "explorer",
    "explorer": "explorer",
    "wordpad": "write",
    "powershell" : "powershell" ,
    
    
    

    # Update this path if VS Code is installed elsewhere
    "vs code": r"C:\Users\Devendra\AppData\Local\Programs\Microsoft VS Code\Code.exe",

    "chrome" : r"C:\Program Files\Google\Chrome\Application\chrome.exe" ,

    "edge" : r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",

    "task manager" : r"%windir%\system32\taskmgr.exe /7" 

 
}

def open_application(command):
    command = command.lower()

    if not command.startswith("open"):
        return False

    for app_name, app_command in APPS.items():

        if app_name in command:

            speak(f"Opening {app_name}")

            try:
                subprocess.Popen(app_command)
            except FileNotFoundError:
                speak(f"I could not find {app_name} on this computer.")

            return True

    return False