import logging

from colorama import Fore, Style

from libs.utils import *


class Log:
    log_debug_msg = False

    is_initialized = False

    log_format = '[%(asctime)s]%(levelname)s: %(message)s'
    date_format = '%Y%m%d %H:%M:%S'
    save_to_file = False
    LOG_FILE = ''

    def __init__(self, log_file_prefix: str = "", level=logging.DEBUG):
        Path("logs").mkdir(parents=True, exist_ok=True)
        self.log_file = "logs/" + log_file_prefix + "_" + platform.node() + "_" + get_current_time_filename() + '.log'
        Log.LOG_FILE = self.log_file

        if len(log_file_prefix) > 1:
            logging.basicConfig(filename=self.log_file,
                                level=level,
                                format=Log.log_format, datefmt=Log.date_format)
            Log.save_to_file = True
        else:
            logging.basicConfig(level=level,
                                format=Log.log_format, datefmt=Log.date_format)
        Log.is_initialized = True
        Log.info("Log Start Timestamp ============")

    @staticmethod
    def get_current_time():
        return str(datetime.fromtimestamp(time.time()).strftime(Log.date_format))

    @staticmethod
    def debug(msg: str, *args):
        if Log.log_debug_msg:
            print(f'{Fore.CYAN}[{Log.get_current_time()}]DEBUG:{Style.RESET_ALL}', msg, *args)
            if Log.save_to_file:
                logging.debug(msg + str(args))

    @staticmethod
    def info(msg: str, *args):
        print(f'{Fore.GREEN}[{Log.get_current_time()}]INFO:{Style.RESET_ALL}', msg, *args)
        if Log.save_to_file:
            logging.info(msg + str(args))

    @staticmethod
    def warning(msg: str, *args):
        print(f'{Fore.YELLOW}[{Log.get_current_time()}]WARNING:{Style.RESET_ALL}', msg, *args)
        if Log.save_to_file:
            logging.warning(msg + str(args))

    @staticmethod
    def error(msg: str, *args):
        print(f'{Fore.RED}[{Log.get_current_time()}]ERROR:{Style.RESET_ALL}', msg, *args)
        if Log.save_to_file:
            logging.error(msg + str(args))


class Debugable:
    def __init__(self):
        self.DEBUG = 1

    def log_debug_msg(self, msg, *args):
        if self.DEBUG:
            Log.debug(msg, *args)