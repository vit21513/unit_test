class Average_two_list:
    def __init__(self, one: list[int | float], two: list[int | float]):
        if isinstance(one, list) and isinstance(two, list):
            self.one = one
            self.two = two
        else:
            raise TypeError

    @property
    def avg_one(self):
        for item in self.one:
            if not isinstance(item, (int, float)):
                raise ValueError(f'Element {item} not int or float')
        if len(self.one):
            return sum(self.one) / len(self.one)
        return 0.0

    @property
    def avg_two(self):
        for item in self.two:
            if not isinstance(item, (int, float)):
                raise ValueError(f'Element {item} not int or float')
        if len(self.two):
            return sum(self.two) / len(self.two)
        return 0.0

    def compare_avg(self):
        if self.avg_one > self.avg_two:
            return f"Первый список имеет большее среднее значение"
        elif self.avg_one < self.avg_two:
            return f"Второй список имеет большее среднее значение"
        return f'Средние значения равны'


