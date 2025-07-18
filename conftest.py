import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Hook for screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            # Attach to report (pytest-html)
            if hasattr(item.config, "_html"):
                extra = getattr(rep, "extra", [])
                extra.append(item.config._html.extras.image(screenshot_path))
                rep.extra = extra


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