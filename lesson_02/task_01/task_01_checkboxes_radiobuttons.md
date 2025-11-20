### Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

1. Открыть страницу https://suninjuly.github.io/math.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x (код для этого приведён ниже).
```python
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
```
4. Ввести ответ в текстовое поле.
5. Отметить checkbox "I'm the robot".
6. Выбрать radiobutton "Robots rule!".
7. Нажать на кнопку Submit.

Для этой задачи понадобится использовать атрибут .text для найденного элемента. 
```python
x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
x = x_element.text
y = calc(x)
```

Время для ввода ответа ограничено.