import re
import sys
import os

from modules.not_valid_point import NotValidPoint

# root project path
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)

# append to sys
sys.path.append(PROJECT_ROOT)


from modules.not_valid_choice import NotValidChoice
import enums


def is_valid_input(pattern, label):
    count_input = 0
    pattern = re.compile(pattern, re.IGNORECASE)
    while True:
        if count_input == enums.TRY_TIME:
            raise NotValidChoice

        string = input(label)
        if re.fullmatch(pattern, string):
            break

        count_input += 1
        print('Invalid choice. Please choose again. ' 
            + f'{enums.TRY_TIME - count_input} times try')
        
    return string