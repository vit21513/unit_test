MIN = 25
MAX = 100


def interval(num: int) -> bool:
    assert type(num) == int, "Это не целое число"
    if MIN <= num <= MAX:
        return True
    return False
