from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertPage(BasePage):

    JS_ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT_TEXT = (By.ID, "result")

    def handle_js_alert(self):
        self.click(self.JS_ALERT_BTN)
        alert = self.driver.switch_to.alert
        alert.accept()
        return "JS Alert handled"

    def handle_js_confirm(self):
        self.click(self.JS_CONFIRM_BTN)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        return "JS Confirm handled"

    def handle_js_prompt(self, message):
        self.click(self.JS_PROMPT_BTN)
        alert = self.driver.switch_to.alert
        alert.send_keys(message)
        alert.accept()
        return self.get_text(self.RESULT_TEXT)
