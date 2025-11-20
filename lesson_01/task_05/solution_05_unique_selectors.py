from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""Проверяем первую страницу, где все обязательные поля отображаются на странице и после их заполнения происходит успешная регистрация"""
try:
    # Ссылка на первую страницу регистрации
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second") 
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    email.send_keys("ivpet@random.com")

    # Нажимаем на кнопку и отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Ждем загрузку страницы и проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # Находим элемент, содержащий текст, подтверждаюший регистрацию
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ставим ожидание, чтобы увидеть сообщение на экране
    time.sleep(5)
    # Закрываем браузер
    browser.quit()

"""Проверяем вторую страницу, где нет поля "Last name" – тест падает, появляется ошибка NoSuchElementException"""
try:
    # Ссылка на вторую страницу регистрации
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля, которые претерпели изменения после "обновления верстки" 
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    first_name.send_keys("Semyon")

    # Тест прерывается на этом этапе т.к. поле отсутствует
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second") 
    last_name.send_keys("Ivanov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    email.send_keys("sivanov@random.com")

    # Нажимаем на кнопку и отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Ждем загрузку страницы и проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # Находим элемент, содержащий текст, подтверждаюший регистрацию
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ставим ожидание, чтобы увидеть сообщение на экране
    time.sleep(5)
    # Закрываем браузер
    browser.quit()