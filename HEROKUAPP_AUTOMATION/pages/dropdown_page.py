from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def select_by_text(self, text):
        select_element = self.wait.until(lambda d: d.find_element(*self.DROPDOWN))
        select = Select(select_element)
        select.select_by_visible_text(text)
        return select.first_selected_option.text

    def select_by_value(self, value):
        select_element = self.wait.until(lambda d: d.find_element(*self.DROPDOWN))
        select = Select(select_element)
        select.select_by_value(value)
        return select.first_selected_option.text
