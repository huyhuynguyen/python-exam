import logging
from logging import FileHandler, Formatter
from logging.handlers import RotatingFileHandler
import os

log_file_path = os.path.join(os.path.dirname(__file__), os.pardir, 'logs')

class MyLogger:
    def __init__(self) -> None:
        self.logger = logging.getLogger('Player log')
        self.logger.setLevel(logging.DEBUG)
        self.formatter = Formatter('%(asctime)s - %(levelname)s - [in %(pathname)s:%(lineno)d] %(message)s')

    def config_log_to_file(self):
        file_handler = FileHandler(filename=f'{log_file_path}/my-log.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

        # file_handler = RotatingFileHandler(filename=f'{log_file_path}/my-log.log', maxBytes=20, backupCount=4)
        # # file_handler.setLevel(logging.DEBUG)
        # file_handler.setFormatter(self.formatter)
        # self.logger.addHandler(file_handler)

    def print_log_to_file(self, point, result):
        self.logger.info(f'Player point: {point}')
        self.logger.info(f'Player {result}')