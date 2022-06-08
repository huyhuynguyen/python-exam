import subprocess
# import enums

import os
import sys

# root project path
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(PROJECT_ROOT)

from modules.my_subprocess_exception import MySubProcessException

def clear_screen():
    # command = enums.CLS_COMMAND_WINDOWS
    try:
        subprocess.run(['clssss'], check=True, shell = True)
    except subprocess.CalledProcessError as e:
        e.stdout = "Command not found"
        return e
    # try:
    #     subprocess.run(command, check=True, shell = True)
    # except OSError:
    #     command_str = {"".join(command)}
    #     raise TypeError(f'"{command_str}" command does not exist')

# print(clear_screen().stdout == "Command not found")
a = clear_screen()