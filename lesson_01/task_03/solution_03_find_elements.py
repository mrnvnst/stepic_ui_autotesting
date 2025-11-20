from selenium import webdriver
from selenium.webdriver.common.by import By
import time

random_text = "Поле заполнено"

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for element in elements:
        element.send_keys(random_text)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

