import subprocess
import enums

def clear_screen():
    command = enums.CLS_COMMAND_WINDOWS
    try:
        subprocess.run(command, check=True, shell = True)
    except subprocess.CalledProcessError as e:
        e.stdout = "Command not found"
        return e

# a = clear_screen()
# if (isinstance(a, subprocess.CalledProcessError)):
#     print(a.stdout)