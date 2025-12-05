import pytest

# scope="class" означает, что фикстура запускается один раз для всего класса:
# перед первым тестом — печатает "^_^"
# после выполнения всех тестов класса — печатает ":3"
# она сработает, только если хотя бы один тест использует её в аргументах.
# Здесь её спрашивают оба теста, значит она точно активна.
# Печатается два смайлика: ^_^ в начале класса и :3 в конце
@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


# обычная фикстура
# выполняется каждый раз, когда указана в аргументах теста.
# используется только в первом тесте.
# Печатается один раз: :)
@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


# фикстура запускается в каждом тесте, даже если её не указывать
# в классе два теста, значит она выполнится два раза
# Печатается: :-Р :-Р
@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        pass

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        pass

# Порядок вывода смайликов:
# ^_^
# :-Р
# :)
# :-Р
# :3
