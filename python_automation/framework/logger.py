import logging
import os
import time

class Logger(object):

    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.debug)

        path = os.path.dirname(os.path.abspath('.'))+ '/logs/'
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        log_name = path+now+'.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.info)

        ch = logging.StreamHandler()
        ch.setLevel(logging.info)

        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return  self.logger
