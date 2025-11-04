import os
import time
from datetime import date

def take_screenshot(driver, name):
    # Base screenshots folder
    base_folder = os.path.join(os.getcwd(), "screenshots")
    
    # Create a subfolder for today's date (e.g., 2025-10-27)
    today_folder = os.path.join(base_folder, date.today().strftime("%Y-%m-%d"))
    os.makedirs(today_folder, exist_ok=True)

    # Generate timestamp for unique filenames
    timestamp = time.strftime("%H%M%S")
    file_path = os.path.join(today_folder, f"{name}_{timestamp}.png")

    # Take screenshot
    driver.save_screenshot(file_path)
    print(f"📸 Screenshot saved: {file_path}")
