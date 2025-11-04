from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def proceed_to_checkout(self):
        print("Clicking Checkout button safely...")
        # Wait until button is clickable
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        # JS click ensures any JS listener works
        self.driver.execute_script("arguments[0].click();", checkout_btn)
        # Wait until URL changes to checkout-step-one.html
        self.wait.until(lambda d: "checkout-step-one.html" in d.current_url)
        print(" Checkout page navigation triggered")
