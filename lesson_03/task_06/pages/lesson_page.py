import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from lesson_03.task_06.pages.base_page import BasePage
from lesson_03.task_06.locators import LessonPageLocators, LoginPopupLocators


class LessonPage(BasePage):

    def click_login_button(self):
        self.wait_clickable(LessonPageLocators.LOGIN_HEADER_BTN).click()
        self.wait_visible(LoginPopupLocators.AUTH_POPUP_FORM)

    def is_field_disabled(self):
        return len(self.driver.find_elements(*LessonPageLocators.ANSWER_FIELD_DISABLED)) > 0

    def is_again_button_visible(self):
        try:
            return self.driver.find_element(*LessonPageLocators.TRY_AGAIN_BUTTON).is_displayed()
        except NoSuchElementException:
            return False

    def reset_if_needed(self):
        if self.is_field_disabled() or self.is_again_button_visible():
            try:
                self.wait_clickable(LessonPageLocators.TRY_AGAIN_BUTTON, 10).click()
            except Exception:
                el = self.wait_presence(LessonPageLocators.TRY_AGAIN_BUTTON)
                self.driver.execute_script("arguments[0].click();", el)

            WebDriverWait(self.driver, 10).until(
                lambda d: not self.is_field_disabled()
            )

    def fill_answer(self, value):
        field = self.wait_visible(LessonPageLocators.ANSWER_FIELD)

        field.click()
        for ch in value:
            field.send_keys(ch)
            time.sleep(0.02)

        self.driver.execute_script(
            """
            arguments[0].dispatchEvent(new Event('input', {bubbles:true}));
            arguments[0].dispatchEvent(new Event('keyup', {bubbles:true}));
            """,
            field
        )

        WebDriverWait(self.driver, 15).until(
            lambda d: d.find_element(*LessonPageLocators.SUBMIT_BTN).is_enabled()
        )

    def click_submit(self):
        btn = self.wait_presence(LessonPageLocators.SUBMIT_BTN)

        self.driver.execute_script("arguments[0].click();", btn)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(LessonPageLocators.HINT_LOCATOR)
        )

    def get_hint_text(self):
        return self.wait_visible(LessonPageLocators.HINT_LOCATOR).text.strip()