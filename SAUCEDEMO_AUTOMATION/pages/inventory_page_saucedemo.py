from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page_saucedemo import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def wait_for_inventory_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
        )

    def add_to_cart(self):
        print(" Trying to click Add to Cart button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

    def go_to_cart(self):
        print(" Trying to click Cart icon")
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        self.driver.execute_script("arguments[0].click();", cart_icon)
        print("Cart icon clicked via JavaScript")

