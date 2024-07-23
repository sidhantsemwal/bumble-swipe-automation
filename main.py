import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from login import login
from like import like

if __name__ == "__main__":
    driver = webdriver.Chrome()

    page_load_timeout=15
    explicit_wait_timeout=15
    driver.set_page_load_timeout(page_load_timeout)
    try:
        wait=WebDriverWait(driver,explicit_wait_timeout)
        driver.get('https://gew3.bumble.com/app')
        print("Opened the website")
    except TimeoutException as e:
        main_page=driver.current_window_handle
        print("the main page handle is : " , main_page)
        button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//span[contains(text(), "Continue with Facebook")]')))
        print("Found the login button")
        button.click()

        time.sleep(5)
        login_page=""
        for handle in driver.window_handles:
            if handle!=main_page:
                login_page=handle
                break
        driver.switch_to.window(login_page)
        login(driver)
        driver.switch_to.window(main_page)
        print("switched back to old window : ", driver.current_window_handle)
        like(driver)

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        print("quitting the driver now ")
        driver.quit()