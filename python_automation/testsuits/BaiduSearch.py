#coding:utf-8
from selenium import webdriver
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
import time
import unittest

class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.browser = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit()
        time.sleep(2)
        try:
            assert 'selenium' in homepage.get_page_title()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.'fromat(e))

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('search')
        homepage.send_submit()
        time.sleep(2)
        homepage.get_page_title()



        # self.driver.find_element_by_id('kw').send_keys('selenium')
        # time.sleep(1)
        # try:
        #     assert 'selenium' in self.driver.title
        #     print('Test pass.')
        # except Exception as e:
        #     print('Test fail.',format(e))

if __name__ == '__main__':
    unittest.main()

        # def open_baidu(self):
    #     self.driver.get("https://www/baidu.com")
    #     time.sleep(1)
    #
    # def test_search(self):
    #     self.search = self.driver.find_element_by_id('kw').clear()
    #     self.search.send_keys('selenium')
    #     self.driver.find_element_by_id('su').click()
    #     time.sleep(1)
    #     print (self.driver.title)
    #     try:
    #         assert 'selenium' in self.driver.title
    #         print ('Test Pass')
    #     except Exception as e:
    #         print ('Test Fail')
    #         self.driver.quit()

# test = BaiduSearch()
# test.open_baidu()
# test.test_search()




