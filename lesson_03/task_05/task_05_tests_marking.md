### Задание: запуск тестов

В этом задании нужно разобраться в маркировках. Мы имеем файл с тестами, которые уже размечены маркерами для разных ситуаций запуска.

**`test_task_run_1.py:`**

```python
import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
```

Выбрать тестовые методы, которые будут найдены и выполнены Pytest при запуске команды: 

```python
pytest -v -m "smoke and not beta_users" test_task_run_1.py
```

<details>

<summary>Ответ</summary>

[x] номер 1

[ ] номер 2

[ ] номер 3

[x] номер 4

[ ] номер 5

[ ] номер 6

[ ] номер 7

</details>