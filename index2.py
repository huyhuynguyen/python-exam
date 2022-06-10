# import modules
# from modules import MyLogger

# my_logger = MyLogger()
# my_logger2 = MyLogger()
# print(f'id index2: {id(my_logger)}')
# print(f'id index2: {id(my_logger2)}')
# my_logger.config_stream_log()
# my_logger.logger.debug('This is a debug log message.')
# my_logger.logger.info('This is a info log message.')
# my_logger.logger.warning('This is a warning log message.')
# my_logger.logger.error('This is a error log message.')
# my_logger.logger.critical('This is a critical log message.')

import random
import subprocess
import sys
import time



# text = "Welcome to guessing game"
# for index, character in enumerate(text):
#     if index == len(text) - 1:
#         print(character, end='\n')
#     else:
#         sys.stdout.write(character)
#         # sys.stdout.flush()
#     time.sleep(0.2)

# print("Start game")

class MyClass:
    __instance = None

    def __new__(cls, *args, **kwds):
        print('new')
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
        

    def __init__(self) -> None:
        print('init')
        pass

a = MyClass()
# b = MyClass()
# print(id(a))
# print(id(b))