import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationPage:
    expected_reg_tex = 'Congratulations! You have successfully registered!'

    def test_first_page_registration_correct_text(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("ivpet@random.com")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        welcome_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text

        assert welcome_text == self.expected_reg_tex

    def test_second_page_registration_correct_text(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("ivpet@random.com")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        welcome_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text

        assert welcome_text == self.expected_reg_tex
        browser.quit()

