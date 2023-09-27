def find_average(lst: list[int | float]) -> float:

    if isinstance(lst,list):
        if len((lst)):
            return sum(lst) / len(lst)
        return 0
    raise TypeError

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(find_average(lst))
