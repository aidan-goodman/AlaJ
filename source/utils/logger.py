from source.utils import config_loader as conf
from pathlib import Path
import datetime
import logging
import os


class Logger:

    def __init__(
        self,
        name,
        level=logging.INFO,
        save=False,
        log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    ):
        """
        初始化Logger类
        :param name: 日志名，通常是模块名
        :param level: 日志级别，默认为INFO
        :param save: 是否保存日志到文件，默认False
        :param log_format: 日志格式，默认为 '%(asctime)s - %(levelname)s - %(message)s'
        """
        self.logger = logging.getLogger(name)
        if not self.logger.hasHandlers():
            formatter = logging.Formatter(log_format)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.setLevel(level)
            self.logger.addHandler(stream_handler)

            if save:
                config = conf.ConfigLoader()
                log_path = os.getcwd() + config.get("log.path")
                Path(log_path).mkdir(parents=True, exist_ok=True)
                today = datetime.date.today().strftime("%Y%m%d")
                log_file = log_path + f"{today}.log"
                Path(log_file).touch(exist_ok=True)

                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                file_handler.setLevel(logging.DEBUG)
                self.logger.addHandler(file_handler)

    def info(self, message):
        """
        记录INFO级别的日志
        :param message: 日志信息
        """
        self.logger.info(message)

    def error(self, message):
        """
        记录ERROR级别的日志
        :param message: 日志信息
        """
        self.logger.error(message)

    def warning(self, message):
        """
        记录WARNING级别的日志
        :param message: 日志信息
        """
        self.logger.warning(message)

    def debug(self, message):
        """
        记录DEBUG级别的日志
        :param message: 日志信息
        """
        self.logger.debug(message)

    def critical(self, message):
        """
        记录CRITICAL级别的日志
        :param message: 日志信息
        """
        self.logger.critical(message)
