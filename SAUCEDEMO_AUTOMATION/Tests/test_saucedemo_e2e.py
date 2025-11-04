import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.login_page_saucedemo import LoginPage
from pages.inventory_page_saucedemo import InventoryPage
from pages.checkout_page_saucedemo import CheckoutPage
from pages.cart_page_saucedemo import CartPage
from utils.screenshot import take_screenshot  # Reuse your screenshot utility


# ✅ POSITIVE SCENARIO – Valid Login and End-to-End Flow
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_saucedemo_e2e(chrome_driver):
    driver = chrome_driver

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # ---- Login ----
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    take_screenshot(driver, "valid_login_success")

    # ---- Inventory ----
    inventory_page.wait_for_inventory_page()
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()
    take_screenshot(driver, "item_added_to_cart")

    # ---- Cart ----
    cart_page.proceed_to_checkout()
    take_screenshot(driver, "proceed_to_checkout")

    # ---- Checkout ----
    checkout_page.fill_checkout_info("Deepika", "S", "600100")
    checkout_page.click_continue()
    checkout_page.click_finish()
    checkout_page.verify_success()
    take_screenshot(driver, "order_completed")



# ⚠️ NEGATIVE SCENARIO – Missing Username Validation
@pytest.mark.negative
def test_missing_username_validation(chrome_driver):
    driver = chrome_driver

    # Step 1: Open login page
    login_page = LoginPage(driver)
    login_page.open_login_page()
    take_screenshot(driver, "login_page_opened")

    # Step 2: Enter only password (no username)
    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("secret_sauce")
    take_screenshot(driver, "entered_password_only")

    # Step 3: Click Login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)
    take_screenshot(driver, "clicked_login_without_username")

    # Step 4: Capture and verify the error message
    try:
        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        print("Displayed Error:", error_message)
        take_screenshot(driver, "missing_username_error")
        assert "Epic sadface: Username is required" in error_message, \
            "❌ BUG FOUND: Expected validation message not displayed!"
        print("✅ Validation working correctly — Username is required message shown.")
    except NoSuchElementException:
        take_screenshot(driver, "error_message_not_found")
        print("❌ BUG FOUND: No validation message displayed.")
        raise
