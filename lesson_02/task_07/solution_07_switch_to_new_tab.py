from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    '''Ловим кнопку и нажимаем на нее'''
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    '''Переходим на новую вкладку'''
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    '''Получаем текст x и вычисляем его значение'''
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    '''Вводим полученное значение x'''
    answer_input = browser.find_element(By.ID, "answer").send_keys(y)
    '''Нажимаем на кнопку Submit'''
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(6)
    browser.quit()

    