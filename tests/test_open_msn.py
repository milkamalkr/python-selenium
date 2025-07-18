from pages.home_page import HomePage
from pages.google_page import GooglePage

def test_msn_homepage_title(driver, test_fixture):
    home_page = HomePage(driver)
    home_page.open_homepage()
    title = home_page.get_title()
    print(f"Page title is: {title}")
    assert "MSNYahoo" in title
 
    print(test_fixture)

def test_google_page_title(driver, test_fixture):
    home_page = GooglePage(driver)
    home_page.open_homepage()
    title = home_page.get_title()
    print(f"Page title is: {title}")
    assert "MSNYahoo" in title
 
    print(test_fixture)