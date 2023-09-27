import pytest

from average import  find_average

def test_find_average():
    lst = [1,2,3,4,5]
    assert find_average(lst) == 3.0, "неправильный расчет среднего"


def test_empty_list():
    assert find_average([]) == 0.0, 'list empty'


def test_find_averagetype():
    lst= '1,2,3,4,5'
    with pytest.raises(TypeError):
        assert find_average(lst)