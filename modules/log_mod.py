import logging
from logging import FileHandler, Formatter, StreamHandler
from logging.handlers import RotatingFileHandler
import os
from modules.singleton import Singleton

log_file_path = os.path.join(os.path.dirname(__file__), os.pardir, 'logs')

class MyLogger(metaclass = Singleton):
    def __init__(self) -> None:
        self.logger = logging.getLogger('Player log')
        self.logger.setLevel(logging.DEBUG)
        self.formatter = Formatter('%(asctime)s - %(levelname)s - [in %(pathname)s:%(lineno)d] %(message)s', datefmt="%Y/%m/%d %H:%M:%S")

    def config_log_to_file(self, filename):
        file_handler = FileHandler(filename=f'{log_file_path}/{filename}.log', delay=True)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

        # file_handler = RotatingFileHandler(filename=f'{log_file_path}/my-log.log', maxBytes=20, backupCount=4)
        # # file_handler.setLevel(logging.DEBUG)
        # file_handler.setFormatter(self.formatter)
        # self.logger.addHandler(file_handler)

    def config_stream_log(self):
        stream_handler = StreamHandler()
        stream_handler.setLevel(logging.ERROR)
        stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(stream_handler)

    def print_log_to_file(self, point, result, filename):
        self.config_log_to_file(filename)
        self.logger.info(f'Player point: {point}')
        self.logger.info(f'Player {result}')

    def print_log_wrong_option_console(self, message):
        self.config_stream_log()
        self.logger.error(message)