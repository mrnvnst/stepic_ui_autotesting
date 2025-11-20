from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x_value = x_element.text
y_value = calc(x_value)

try: 
    y_input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", y_input)
    y_input.send_keys(y_value)
    choose_checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    choose_radiobutton = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()

