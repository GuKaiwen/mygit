import configparser
import os
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exr'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        config = configparser.ConfigParser()
        config_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(config_path)

        browser = config.get('browser type','browser name')
        logger.info('you had select %s browser'%browser)
        url = config.get('server URL','URL')
        logger.info('The Test server url is :%s'%url)

        if browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info('Starting Firefox Browser.')
        elif browser == 'IE':
            driver = webdriver.IE(self.ie_driver_path)
            logger.info('Starting IE Browser.')

        driver.get(url)
        logger.info('open Url %s'%url)
        driver.maxmize_window()
        logger.info('Maxmize th current window')
        driver.implicitly_wait(10)
        logger.info('Ser implicitly wait 10 Seconds.')

    def quit_browsr(self):
        logger.info('Now,close and quit the browser')
        self.driver.quit()


