import pytest

from lesson_03.task_06.pages.lesson_page import LessonPage
from lesson_03.task_06.pages.login_popup import LoginPopup
from lesson_03.task_06.data import UserData, TestUrls
from lesson_03.task_06.utility import ComputeAnswer


class TestStepikAuthorization:

    @pytest.mark.parametrize("url", TestUrls.urls)
    def test_compare_hint_text_after_answer_submit(self, driver, url):
        driver.get(url)

        lesson_page = LessonPage(driver)
        login_popup = LoginPopup(driver)

        lesson_page.click_login_button()
        login_popup.login(UserData.user_email, UserData.user_password)

        lesson_page.reset_if_needed()

        answer = ComputeAnswer.compute_answer()
        lesson_page.fill_answer(answer)
        lesson_page.click_submit()

        hint = lesson_page.get_hint_text()

        assert "Correct" in hint, f"На странице {url} неверный ответ: {hint}"

