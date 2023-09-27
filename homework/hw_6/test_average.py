import pytest
from average import Average_two_list


@pytest.fixture()
def setup():
    list1 = [1, 2, 3, 5]
    list2 = [5, 4, 5]
    return list1, list2


def test_compare_average(setup):
    """ тест на правильный результат"""
    lst1, lst2 = setup
    assert Average_two_list(lst1,
                            lst2).compare_avg() == 'Второй список имеет большее среднее значение', "неправильное сравнение"
    assert Average_two_list(lst2,
                            lst1).compare_avg() == 'Первый список имеет большее среднее значение', "неправильное сравнение"
    assert Average_two_list(lst1, lst1).compare_avg() == 'Средние значения равны', "неправильное сравнение"


def test_empty_list():
    "тест на пустые списки "
    assert Average_two_list([], []).compare_avg() == 'Средние значения равны', 'неправильное сравнение'

    assert Average_two_list([2, 2, 2],
                            []).compare_avg() == 'Первый список имеет большее среднее значение', 'неправильное сравнение'
    assert Average_two_list([],
                            [2, 2,
                             2]).compare_avg() == 'Второй список имеет большее среднее значение', 'неправильное сравнение'


def test_find_average_type():
    "тест на некорректый аргумент"
    lst = '1,2,3,4,5'
    with pytest.raises(TypeError):
        assert Average_two_list(lst, [])



def test_creaty_class():
    "тест на некорректный тип аргумента"
    with pytest.raises(TypeError):
        assert Average_two_list("1,2,3,4", [3, 4])



def test_missing_argum():
    "тест на количество аргументов"
    with pytest.raises(TypeError):
        assert Average_two_list([3, 4])



def test_value_type():
    "тест на корректность  переданнх типов даннх"
    with pytest.raises(ValueError):
        assert Average_two_list(["d", 4, "d"], []).avg_one

