from github.lab3.lab_python_fp.gen_random import gen_random


class Unique:
    """Итератор, оставляющий только уникальные значения."""
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.items = items
        self.index = 0
        self.ignore_case = [kwargs[key] for key in kwargs] if len(kwargs) > 0 and kwargs['ignore_case'] is True \
            else False

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.items):
                raise StopIteration
            else:
                #if self.ignore_case:
                    #self.items = list(map(lambda _: str(_).lower(), self.items))
                if self.ignore_case:
                    current = str(self.items[self.index]).lower()
                else:
                    current = self.items[self.index]
                self.index += 1
                if current not in self.used_elements:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_elements.add(current)
                    return current


if __name__ == '__main__':
    print('Task 1')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item, end=' ')

    print('\nTask 2')
    data = gen_random(5, 3, 10)
    print(*data, sep=', ')
    for item in Unique(data):
        print(item, end=' ')

    print('\nTask 3')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data):
        print(item, end=' ')

    print('\nTask 4')
    for item in Unique(data, ignore_case=True):
        print(item, end=' ')
