import pages
import pages.base_page

class GooglePage(pages.base_page.BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_homepage(self):
        self.open_url("http://www.google.com")