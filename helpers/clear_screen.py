import subprocess
import enums

def clear_screen():
    command = enums.CLS_COMMAND_WINDOWS
    try:
        subprocess.run(command, check=True, shell = True)
    except subprocess.SubprocessError as e:
        print('Command not found')