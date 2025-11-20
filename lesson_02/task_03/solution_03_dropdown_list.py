from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


link_1 = "https://suninjuly.github.io/selects1.html"
link_2 = "https://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link_1)

num_1 = browser.find_element(By.ID, "num1").text
num_2 = browser.find_element(By.ID, "num2").text
total_value = int(num_1) + int(num_2)

"""Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select. 
Далее можно найти любой вариант из списка с помощью метода select_by_value(value)"""
dropdown_list = Select(browser.find_element(By.ID, "dropdown"))

try:
    """Преобразуем в строку, т.к. метод работает со строковым параметром"""
    dropdown_list.select_by_value(str(total_value))
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:    
    time.sleep(6)
    browser.quit()

