import time
from selenium import webdriver
from swipe import swipe_automate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    
    driver = webdriver.Chrome()
    try:
    # Open the website
        driver.get('https://gew3.bumble.com/app')
        print("Opened the website")

        # Wait for the "like" button to be clickable
        button = driver.find_element(By.XPATH, '//span[contains(text(), "Continue with Facebook")]')
        print("Found the login button")

        # Click the "like" button
        button.click()
        print("Login successful")

        count = 0
        while count < 10:
            # Wait for the "like" button to be clickable
            button = driver.find_element(By.XPATH, '//span[contains(text(), "Continue with Facebook")]')
            # Click the "like" button
            button.click()
            print(f"Clicked like button {count + 1}")
            count += 1
            time.sleep(10)  # Adjust as needed based on the site's responsiveness

        print("Finished liking profiles")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        # Close the browser session
        driver.quit()