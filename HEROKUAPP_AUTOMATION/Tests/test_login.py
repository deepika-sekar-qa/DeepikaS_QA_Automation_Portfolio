# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot 

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("tomsmith", "SuperSecretPassword!", True),
        ("tomsmith", "wrongpass", False),
        ("wronguser", "SuperSecretPassword!", False)
    ]
)
def test_login(chrome_driver, username, password, expected):
    driver = chrome_driver
    login_page = LoginPage(driver)
    login_page.open()
    take_screenshot(driver, "login_page_opened")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    

    flash_text = login_page.get_success_message()
    try:
        if expected:
            assert "You logged into a secure area!" in flash_text
            take_screenshot(driver, f"login_success_{username}")
        else:
            assert "Your username is invalid!" in flash_text or "Your password is invalid!" in flash_text
            take_screenshot(driver, f"login_invalid_{username}")
    except AssertionError:
        take_screenshot(driver, f"login_fail_{username}")
        raise
