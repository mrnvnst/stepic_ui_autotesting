from lesson_03.task_06.pages.base_page import BasePage
from lesson_03.task_06.locators import LoginPopupLocators 


class LoginPopup(BasePage):

    def login(self, email, password):
        self.wait_visible(LoginPopupLocators.EMAIL_INPUT).send_keys(email)
        self.wait_visible(LoginPopupLocators.PASSWORD_INPUT).send_keys(password)
        self.wait_clickable(LoginPopupLocators.LOGIN_SUBMIT_BTN).click()
        self.wait_presence(LoginPopupLocators.EMAIL_INPUT)