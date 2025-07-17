class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def open_url(self, url):
        self.driver.get(url)
