from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_TEXT = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _react_type(self, locator, value):
        """React-safe typing method that updates Virtual DOM state"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.2)

        # Focus field
        self.driver.execute_script("arguments[0].focus();", element)
        time.sleep(0.2)

        # Clear any existing text
        element.clear()
        time.sleep(0.2)

        # Set value and trigger React synthetic event
        self.driver.execute_script("""
            const [el, val] = arguments;
            const lastVal = el.value;
            el.value = val;
            const event = new Event('input', { bubbles: true });
            event.simulated = true;

            // React 17+ internal event tracker
            const tracker = el._valueTracker;
            if (tracker) tracker.setValue(lastVal);

            el.dispatchEvent(event);
        """, element, value)

        time.sleep(0.4)
        self.driver.execute_script("arguments[0].blur();", element)
        time.sleep(0.3)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        print(" Filling checkout info (React-safe typing)...")
        self._react_type(self.FIRST_NAME, first_name)
        self._react_type(self.LAST_NAME, last_name)
        self._react_type(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        print("Clicking Continue button...")
        btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def click_finish(self):
        print("Clicking Finish button...")
        btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)

    def verify_success(self):
        print("Verifying success message...")
        success = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TEXT))
        assert "THANK YOU" in success.text.upper(), "Checkout failed"
        print("Checkout successful!")

        self.driver.save_screenshot("checkout_success.png")
        print("Screenshot saved as checkout_success.png")
