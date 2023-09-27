import random


# class RandomGen:
#
#     def __init__(self):
#         self._num = [random.randint(0,100) for _ in range(random.randint(0,10))]
#
#     @property
#     def get_num(self):
#         return self._num
#


def random_list():
    return [random.randint(0,100) for _ in range(random.randint(2,10))]

