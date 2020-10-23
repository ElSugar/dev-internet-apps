from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, input_length, input_colour):
        self.length = input_length

        # Вызывается constructor родительского класса (Rectangle)
        # чтобы прикрепить значения к атрибутам родительского класса.
        super().__init__(self.length, self.length, input_colour)

    @classmethod
    def get_name(cls):
        return 'Квадрат'

    def __repr__(self):
        return '{} {} цвета со стороной {} имеет площадь {}'.format(self.get_name(), self.colour.colour_property,
                                                                    self.length, self.area())

