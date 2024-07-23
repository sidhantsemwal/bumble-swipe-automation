from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import constants 
import time

def like(driver:webdriver):
    max_likes = constants.MAX_LIKES
    timeout=5
    count=0
    while count < max_likes:
        like_button = WebDriverWait(driver,timeout).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"encounters-action--like")))
        like_button.click()
        count+=1
        print(f"Clicked like button {count} times")
        time.sleep(timeout) 

    print("Finished liking profiles")