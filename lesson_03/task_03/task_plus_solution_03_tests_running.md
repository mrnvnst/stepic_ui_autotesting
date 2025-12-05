### Задание: запуск тестов

##### Ниже представлен тестовый проект. Нужно определить какие тестовые методы будут найдены и выполнены PyTest.
---
Директория:

**`tests_for_pytest/test_main_page:`**

- номер 1

```python
def main_page_buttons(browser):
```

- номер 2

```python
def test_main_page_navbar(browser):
```

----
              
Директория:

**`smoke_tests/login.py:`**

- номер 3

```python
def test_guest_can_login(browser, language):
```

- номер 4

```python 
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
```
---
                  
Корневая директория проекта:
 
 **`test_regression.py:`**


`class TestLessonCreate():`


- номер 5

```python
def test_create_lesson(self, browser):
```

- номер 6

```python
def user_with_lesson_can_create_lesson_from_navbar_test(self, browser):
```

`class CourseCreate():`

- номер 7
    
```python
def test_create_course(self, browser):
```

- номер 8

```python
def test_guest_can_open_new_course(browser):
```
---

<details>

<summary>Ответ</summary>

[ ] номер 1

[ ] номер 2

[ ] номер 3

[ ] номер 4

[x] номер 5

[ ] номер 6

[ ] номер 7

[x] номер 8

</details>