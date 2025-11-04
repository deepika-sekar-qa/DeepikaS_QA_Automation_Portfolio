from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    DROPDOWN_LINK = (By.LINK_TEXT, "Dropdown")
    ALERTS_LINK = (By.LINK_TEXT, "JavaScript Alerts")
    DYNAMIC_LOADING_LINK = (By.LINK_TEXT, "Dynamic Loading")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def go_to_dropdown(self):
        self.click(self.DROPDOWN_LINK)

    def go_to_alerts(self):
        self.click(self.ALERTS_LINK)

    def go_to_dynamic_loading(self):
        self.click(self.DYNAMIC_LOADING_LINK)
