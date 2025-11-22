import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(unittest.TestCase):
    expected_reg_tex = 'Congratulations! You have successfully registered!'

    # метод для заполнения полей
    def fill_required_fields(self, browser):

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivpet@random.com")
    
    # метод для клика по кнопке и получения текста об успешности регистрации
    def submit_and_get_text(self, browser):
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        welcome_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text

        return welcome_text

    # тест для первой страницы – OK
    def test_first_page_registration_correct_text(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        self.fill_required_fields(browser)
        welcome_text = self.submit_and_get_text(browser)

        browser.quit()

        self.assertEqual(welcome_text, self.expected_reg_tex)

    # тест для второй страницы – ERROR (NoSuchElementException)
    def test_second_page_registration_correct_text(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        self.fill_required_fields(browser)
        welcome_text = self.submit_and_get_text(browser)

        browser.quit()

        self.assertEqual(welcome_text, self.expected_reg_tex)


if __name__ == "__main__":
    unittest.main()