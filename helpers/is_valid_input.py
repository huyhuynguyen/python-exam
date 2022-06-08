import re
import enums

def is_valid_input(pattern, label):
    count_input = 0
    pattern = re.compile(pattern, re.IGNORECASE)
    while True:
        if count_input == enums.TRY_TIME:
            raise ValueError(enums.INVALID_INPUT)

        string = input(label)
        if not re.fullmatch(pattern, string):
            count_input += 1
            print(f'Invalid choice. Please choose again. {enums.TRY_TIME - count_input} times try')
        else:
            break
    return string