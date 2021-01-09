from abc import ABCMeta, abstractstaticmethod


class ICakeBuilder(metaclass=ABCMeta):
    """Интерфейс строителя"""

    @abstractstaticmethod
    def set_foundation(self, value):
        """Задает основу для торта"""

    @abstractstaticmethod
    def set_shape_type(self, value):
        """Задает форму для торта"""

    @abstractstaticmethod
    def set_filling(self, value):
        """Задает тип начинки"""

    @abstractstaticmethod
    def set_number_tiers(self, value):
        """Задает количество ярусов торта"""

    @abstractstaticmethod
    def get_result(self):
        """Возвращает торт"""


class CakeBuilder(ICakeBuilder):
    """Конкретный строитель"""

    def __init__(self):
        self.cake = Cake()

    def set_foundation(self, value):
        self.cake.foundation = value
        return self

    def set_shape_type(self, value):
        self.cake.shape_type = value
        return self

    def set_filling(self, value):
        self.cake.filling = value
        return self

    def set_number_tiers(self, value):
        self.cake.tiers = value
        return self

    def get_result(self):
        return self.cake


class Cake:
    """Торт"""

    def __init__(self, foundation='бисквитный', shape_type='круга', filling='шоколадная', tiers=1):
        # бисквитный, песочный, слоеный, шоколадный
        self.foundation = foundation
        # круг, овал, квадрат, сердце, ромб, звезда
        self.shape_type = shape_type
        # шоколадная, клубничная, вишневая, йогуртовая, ореховая
        self.filling = filling
        self.tiers = tiers

    def __str__(self):
        return 'Это {0} торт в форме {1} с {2} начинкой и {3} ярусами.'.format(
            self.foundation, self.shape_type, self.filling, self.tiers
        )


class YogurtDirector:
    @staticmethod
    def construct():
        return CakeBuilder()\
            .set_foundation('бисквитный')\
            .set_shape_type('овала')\
            .set_filling('йогуртовой')\
            .set_number_tiers(3)\
            .get_result()


class StrawberryDirector:
    @staticmethod
    def construct():
        return CakeBuilder()\
            .set_foundation('бисквитный')\
            .set_shape_type('сердца')\
            .set_filling('клубничной')\
            .set_number_tiers(1)\
            .get_result()


class ChocolateDirector:
    @staticmethod
    def construct():
        return CakeBuilder()\
            .set_foundation('шоколадный')\
            .set_shape_type('квадрата')\
            .set_filling('ореховой')\
            .set_number_tiers(1)\
            .get_result()


if __name__ == '__main__':
    YOGURT_CAKE = YogurtDirector.construct()
    print(YOGURT_CAKE)
    STRAWBERRY_CAKE = StrawberryDirector.construct()
    print(STRAWBERRY_CAKE)
    CHOCOLATE_CAKE = ChocolateDirector.construct()
    print(CHOCOLATE_CAKE)
