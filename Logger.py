# Logging function, output to file all.log.

import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='debug', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        logging.basicConfig()
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        #th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
        #                                       encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        #th.setFormatter(format_str)
        # self.logger.addHandler(sh)
        # self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('gateway', level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('warn')
    log.logger.error('error')
    log.logger.critical('fatal')
    Logger('error.log', level='error').logger.error('error')
