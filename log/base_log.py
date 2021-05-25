import logging
import colorlog
import time
import os


class Log(object):

    def __init__(self):
        log_colors_config = {
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }


        # 创建logger
        self.logger = logging.getLogger()

        # 日志输出格式
        self.file_Formatter = logging.Formatter(
            fmt='[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
            datefmt='%Y-%m-%d  %H:%M:%S'
        )
        self.console_Formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %('
                'message)s',
            datefmt='%Y-%m-%d  %H:%M:%S',
            log_colors=log_colors_config
        )

        # 输出控制台
        self.console_Handler = logging.StreamHandler()


        path = 'logger-' + time.strftime('%Y-%m-%d') + '.log'
        print(path)
        # 输出文件
        self.file_Handler = logging.FileHandler(filename=path,  mode='a', encoding='utf8')

    def _console(self, level, msg):
        # 设置级别
        self.logger.setLevel(logging.DEBUG)
        self.console_Handler.setLevel(logging.DEBUG)
        self.file_Handler.setLevel(logging.DEBUG)

        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.file_Handler)
        self.logger.addHandler(self.console_Handler)

        self.file_Handler.setFormatter(self.file_Formatter)
        self.console_Handler.setFormatter(self.console_Formatter)
        if level == 'info':
            self.logger.info(msg)
        elif level == 'debug':
            self.logger.debug(msg)
        elif level == 'warning':
            self.logger.warning(msg)
        elif level == 'error':
            self.logger.error(msg)
        elif level == 'critical':
            self.logger.critical(msg)

    def debug(self, msg):
            self._console(level='debug', msg=msg)

    def info(self, msg):
            self._console(level='info', msg=msg)

    def warning(self, msg):
            self._console(level='warming', msg=msg)

    def error(self, msg):
            self._console(level='error', msg=msg)

    def critical(self, msg):
            self._console(level='critical', msg=msg)


if __name__ == '__main__':
    log = Log()
    log.info('helow')
    log.debug('helow')
    log.error('helow')
    log.warning('helow')
    log.critical('helow')

