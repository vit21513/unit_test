# def calculator(a: int, b: int, operand: str):
#     match operand:
#         case "+":
#             return a + b
#         case "-":
#             return a - b
#         case "*":
#             return a * b
#         case "/":
#             return a / b
from math import sqrt


def square_root(num: float)-> float:
    # assert num > 0, 'number must greater 0'
    if num < 0:
        raise Exception(f"number {num} must greater 0")
    return sqrt(num)


def test_square_root_positive():
    assert square_root(25) == 5,"test not pass"

def test_square_root_zero():
    assert square_root(0) == 0,"test  this zero is not pass"

def test_square_root_negative():
    try:
        square_root(-5)
        raise Exception("ожидалась ошибка, вычиление не возможно")
    except Exception:
        print('test passed')


if __name__ == '__main__':
    # print(calculator(10, 2, "+"))
    # print(calculator(6, 2, "/"))
    # assert 8 == calculator(4,5,'+'),"exeption in method"
    # print(square_root(-5))
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()
