from selenium import webdriver
from selenium.webdriver.common.by import By

import os  
import time


link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))  
file_name = "file_for_task_05.txt"
file_path = os.path.join(current_dir, file_name) 

name_input = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='firstname']")
last_name_input = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='lastname']")
email_input = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='email']")
file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

try:
    name_input.send_keys("Ivan")
    last_name_input.send_keys("Petrov")
    email_input.send_keys("ivpettest@yahoo.com")
    file_button.send_keys(file_path)
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit

