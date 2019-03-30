from framework.base_page import BasePage

class SportNewsHomePage(BasePage):
    nba_link = 'xpath =>//*[@id="col_nba"]/div[1]/div[1]/div/h2/span[1]'

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
