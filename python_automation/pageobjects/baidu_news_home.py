from framework.base_page import BasePage

class NewsHomePage(BasePage):
    sport_link = 'xpath =>//*[@id="channel-shanghai"]/div/ul/li[7]/a'

    def click_sport(self):
        self.click(self.sport_link)
        self.sleep(2)
