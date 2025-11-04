from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):

    START_BUTTON = (By.XPATH, "//div[@id='start']/button")
    FINISH_TEXT = (By.ID, "finish")
    EXAMPLE2_LINK = (By.LINK_TEXT, "Example 2: Element rendered after the fact")

    def open_example2(self):
        self.click(self.EXAMPLE2_LINK)

    def start_loading(self):
        self.click(self.START_BUTTON)
        return self.get_text(self.FINISH_TEXT)
        
        
