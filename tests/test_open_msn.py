from pages.home_page import HomePage

def test_msn_homepage_title(driver, test_fixture):
    home_page = HomePage(driver)
    home_page.open_homepage()
    title = home_page.get_title()
    print(f"Page title is: {title}")
    assert "MSN" in title
 
    print(test_fixture)