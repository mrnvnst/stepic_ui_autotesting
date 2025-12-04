from selenium.webdriver.common.by import By

class LessonPageLocators:
    LOGIN_HEADER_BTN = (By.CSS_SELECTOR, "a.navbar__auth_login[href*='auth=login']")
    ANSWER_FIELD = (By.CSS_SELECTOR, "textarea.string-quiz__textarea")
    ANSWER_FIELD_DISABLED = (By.CSS_SELECTOR, "textarea.string-quiz__textarea[disabled]")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button.submit-submission")
    TRY_AGAIN_BUTTON = (By.CSS_SELECTOR, "button.again-btn.white")
    HINT_LOCATOR = (By.CSS_SELECTOR, "div.smart-hints__hint")

class LoginPopupLocators:
    AUTH_POPUP_FORM = (By.CSS_SELECTOR, "form#login_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login_email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login_password")
    LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, "form#login_form button[type='submit']")

