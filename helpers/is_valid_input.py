import re
import enums

def is_valid_input(pattern, label):
    count_input = 0
    pattern = re.compile(pattern, re.IGNORECASE)
    while True:
        try:
            if count_input == enums.TRY_TIME:
                raise ValueError
        except ValueError:
            print(enums.INVALID_INPUT)
            return ValueError

        string = input(label)
        if re.fullmatch(pattern, string):
            break

        count_input += 1
        print(f'Invalid choice. Please choose again. {enums.TRY_TIME - count_input} times try')
        
    return string