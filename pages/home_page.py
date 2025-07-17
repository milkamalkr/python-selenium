from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_homepage(self):
        self.open_url("https://www.msn.com")
