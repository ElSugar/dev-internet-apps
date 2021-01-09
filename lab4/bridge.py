from abc import ABCMeta, abstractmethod


class Decoration(metaclass=ABCMeta):
    """Декорирование"""

    @abstractmethod
    def decorating_strawberry_cake(self, items):
        """Клубничный торт"""

    @abstractmethod
    def decorating_chocolate_cake(self, items):
        """Шоколадный торт"""


class Candle(Decoration):
    """Декорирование свечами"""

    def decorating_strawberry_cake(self, items):
        return f"Клубничный торт с {items} свечами."

    def decorating_chocolate_cake(self, items):
        return f"Шоколадный торт с {items} свечами."


class Flower(Decoration):
    """Декорирование цветами"""

    def decorating_strawberry_cake(self, items):
        return f"Клубничный торт с {items} цветами."

    def decorating_chocolate_cake(self, items):
        return f"Шоколадный торт с {items} цветами."


class Cake(metaclass=ABCMeta):
    """Торт"""

    @abstractmethod
    def __init__(self, decoration):
        self.decoration = decoration

    @abstractmethod
    def display_description(self):
        """Выводит информацию"""

    @abstractmethod
    def add_objects(self):
        """Добавляет объект декора"""


class Strawberry(Cake):
    def __init__(self, decoration, objects=0):
        super().__init__(decoration)
        self.objects = objects

    def display_description(self):
        return self.decoration.decorating_strawberry_cake(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


class Chocolate(Cake):
    def __init__(self, decoration, objects=0):
        super().__init__(decoration)
        self.objects = objects

    def display_description(self):
        return self.decoration.decorating_chocolate_cake(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


if __name__ == '__main__':
    candle = Candle()
    flower = Flower()

    chocolate1 = Chocolate(candle, 20)
    chocolate2 = Chocolate(flower, 2)
    strawberry1 = Strawberry(candle, 4)
    strawberry2 = Strawberry(flower, 50)

    print(strawberry1.display_description())
    strawberry1.add_objects(1)
    print(strawberry1.display_description())

    print(chocolate1.display_description())
    print(chocolate2.display_description())
    print(strawberry2.display_description())
