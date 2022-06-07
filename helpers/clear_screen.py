import subprocess
import enums

def clear_screen():
    command = enums.CLS_COMMAND_WINDOWS
    try:
        subprocess.run(command, check=True, shell = True)
    except:
        command_str = {"".join(command)}
        raise TypeError(f'"{command_str}" command does not exist')