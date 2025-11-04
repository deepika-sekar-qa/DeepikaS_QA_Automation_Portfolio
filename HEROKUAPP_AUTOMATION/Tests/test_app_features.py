import pytest
from pages.home_page import HomePage
from pages.dropdown_page import DropdownPage
from pages.alert_page import AlertPage
from pages.dynamic_loading_page import DynamicLoadingPage
from utils.screenshot import take_screenshot 


class TestHerokuApp:

    def test_herokuapp_all(self, chrome_driver):
        driver = chrome_driver
        home = HomePage(driver)
        home.open()
        take_screenshot(driver,"home_page_opened")

        # ---------------- Dropdown ----------------
        home.go_to_dropdown()
        dropdown = DropdownPage(driver)
        assert dropdown.select_by_text("Option 1") == "Option 1"
        assert dropdown.select_by_value("2") == "Option 2"
        take_screenshot(driver,"dropdown_selected_options")
        driver.back()

        # ---------------- Alerts ----------------
        home.go_to_alerts()
        alert_page = AlertPage(driver)
        assert alert_page.handle_js_alert() == "JS Alert handled"
        assert alert_page.handle_js_confirm() == "JS Confirm handled"
        assert "Deepika - QA Tester" in alert_page.handle_js_prompt("Deepika - QA Tester")
        take_screenshot(driver,"alerts_all_handled")
        driver.back()

        # ---------------- Dynamic Loading ----------------
        home.go_to_dynamic_loading()
        dyn_page = DynamicLoadingPage(driver)
        dyn_page.open_example2()
        take_screenshot(driver,"dynamic_loading_page_opened")
        assert dyn_page.start_loading() == "Hello World!"
        take_screenshot(driver,"dynamic_loading_completed")
