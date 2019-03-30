import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.new_sport_home import SportNewsHomePage
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage

class ViewNbaNews(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def testViewNbaNews(self):
        baiduhome = HomePage(self.driver)
        baiduhome.click_news()

        newshome = NewsHomePage(self.driver)
        newshome.click_sport()

        sportnewhome = SportNewsHomePage(self.driver)
        sportnewhome.click_nba_link()


if __name__ == '__main__':
    unittest.main()


