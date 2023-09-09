def calculator_discount(cash, discount):
    try:
        if cash > 0 and 0 < discount <= 100:
            return cash - cash * discount / 100
        else:
            raise ArithmeticError(
                """Параметры не могут быть отрицательными либо равны 0,
                а также скидка не может больше 100%""")
    except TypeError:
        return f'недопустимый тип аргументов'


def test_calculator_discount_result(cash=1000, discount=5):
    assert calculator_discount(cash, discount) == 950.0, "тест на верный расчет не пройден"


def test_calculator_check_discount(cash=1000, discount=120):
    assert calculator_discount(cash, discount), "тест не пройден, размер скидки более 100%"


def test_calculator_discount_positive(cash=-1000, discount=-12):
    assert calculator_discount(cash, discount), "тест  не пройден, параметры меньше нуля"


if __name__ == "__main__":
    print(calculator_discount(10, 10))
    test_calculator_check_discount()
    # test_calculator_discount_positive()
    # test_calculator_discount_result()
