from abc import ABCMeta, abstractstaticmethod


class ICake(metaclass=ABCMeta):
    """Интерфейс обработки запросов"""

    @abstractstaticmethod
    def set_successor(successor):
        """Установка следующего обработчика в цепочке"""

    @abstractstaticmethod
    def handle(amount):
        """Обработка события"""


class BigCake(ICake):
    """Конкретный торт
    Выдает большой торт весом 5 кг, если применимо,
    в противном случае продолжает """

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        """Установка преемника"""
        self._successor = successor

    def handle(self, amount):
        """Обработка торта"""
        if amount >= 5:
            num = amount // 5
            remainder = amount % 5
            print(f'Больших тортов весом 5 кг -- {num}')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class MediumCake(ICake):
    """Конкретный торт
    Выдает большой торт весом 3 кг, если применимо,
    в противном случае продолжает """

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        """Установка преемника"""
        self._successor = successor

    def handle(self, amount):
        """Обработка торта"""
        if amount >= 3:
            num = amount // 3
            remainder = amount % 3
            print(f'Средних тортов весом 3 кг -- {num}')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class SmallCake(ICake):
    """Конкретный торт
    Выдает большой торт весом 1 кг, если применимо,
    в противном случае продолжает """

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        """Установка преемника"""
        self._successor = successor

    def handle(self, amount):
        """Обработка торта"""
        if amount >= 1:
            num = amount // 1
            remainder = amount % 1
            print(f'Маленьких тортов весом 1 кг -- {num}')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class CakeChain:
    """Связь тортов"""

    def __init__(self):
        self.chain1 = BigCake()
        self.chain2 = MediumCake()
        self.chain3 = SmallCake()

        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


if __name__ == '__main__':
    CAKES = CakeChain()
    AMOUNT = int(input('Введите желаемую сумму всех тортов: '))
    if AMOUNT < 1:
        print('Введите положительное число')
        exit()
    CAKES.chain1.handle(AMOUNT)
    print('Готово!')
