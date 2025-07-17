import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    # Setup Chrome driver
    service=Service(r'D:\Selenium_venv\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # Optional: run in headless mode
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def test_fixture():
    return "test"