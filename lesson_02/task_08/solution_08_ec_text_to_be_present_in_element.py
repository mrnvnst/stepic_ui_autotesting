from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    '''Ждем, пока цена будет $100'''
    check_price = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    '''Ждем, кнопка Book станет кликабельна и нажимаем ее'''
    browser.find_element(By.ID, "book").click()
    '''Получаем текст x и вычисляем его значение'''
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    '''Вводим полученное значение x'''
    answer_input = browser.find_element(By.ID, "answer").send_keys(y)
    '''Нажимаем на кнопку Submit'''
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(15)
    browser.quit()

    