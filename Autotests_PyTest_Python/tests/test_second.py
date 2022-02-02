import pytest


# метод деления чисел
def division(a, b):
    return a / b


# тест на соответствие
def test_equal():
    assert division(25, 5) == 5, "Результат деления чисел 25 / 5 должно быть 5"


# тест на исключение
def test_not_equal():
    with pytest.raises(ZeroDivisionError) as error:
        division(25, 0)
    assert 'division by zero' == error.value.args[0], "Сообщение division by zero - при делении на ноль "


# Запуск всех тестов
if __name__ == '__main__':
    pytest.main()
