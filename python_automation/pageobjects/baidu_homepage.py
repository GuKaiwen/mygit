from framework.base_page import  BasePage

class HomePage(BasePage):
    input_box = 'id=>kw'
    search_submit = 'xpath=>//*[@id='su']'
    news_link = 'xpath=>//*[@id="u_sp"]/a[1]'

    def type_search(self, text):
        self.type(self.input_box,text )

    def send_submit(self):
        self.click(self.search_submit)

    def click_news(self, selector):
        self.click(self.news_link)
        self.sleep(2)