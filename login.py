from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import constants 
import time
from LoginError import LoginError

def login(driver: webdriver.Chrome):
    try:
        print("entered login function")
        login_page=driver.current_window_handle
        print("The Login page handle is : ", login_page)
        timeout=10
        email= WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located((By.ID,'email')))
        email.send_keys(constants.EMAIL)
        print("wrote the email")

        password = WebDriverWait(driver,timeout).until(expected_conditions.visibility_of_element_located((By.ID,'pass')))
        password.send_keys(constants.PASSWORD)
        print("wrote the password")

        login_button = WebDriverWait(driver,timeout).until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@value='Log in']")))
        login_button.click()
        print("login button clicked")
        time.sleep(15)
        if(login_page in driver.window_handles):
            raise LoginError(f"The Email-ID or password is incorrect") 
    except LoginError as e:
        print(e.message)
        driver.quit()
        return
    except Exception as e:
        print("An unknown exception has occured : " , e)
        driver.quit()
        return
    else:
        print("the login was successful. No errors ")
    finally: 
        print("Exiting the login page now.")
