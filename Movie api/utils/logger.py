import logging
from utils.config import Config
from environment import Router

class Logger:
    CONFIG_KEY = 'log'

    @staticmethod
    def get_level():
        if Router.current_environ == "dev":return "DEBUG"
        elif Router.current_environ == "prod": return "INFO"

        return Config.read(Logger.CONFIG_KEY, 'level')

    @staticmethod
    def get_filename():
        return Config.read(Logger.CONFIG_KEY,'filename')
    
    @staticmethod
    def get_date_format():
        return Config.read(Logger.CONFIG_KEY, 'dateFormat')
    
    @staticmethod
    def get_format():
        return Config.read(Logger.CONFIG_KEY, 'format')
    
    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(Logger.get_level())

        formatter = logging.Formatter(
            Logger.get_format(),
            Logger.get_date_format()
        )
        file_hdlr = logging.FileHandler(Logger.get_filename())
        file_hdlr.setFormatter(formatter)
        logger.addHandler(hdlr=file_hdlr)

        return logger