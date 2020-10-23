from lab_python_oop.geometric_figure import Figure
from lab_python_oop.colour import Colour


class Rectangle(Figure):
    def __init__(self, input_width, input_height, input_colour):
        self.width = input_width
        self.height = input_height
        self.colour = Colour()
        self.colour.colour_property = input_colour

    @classmethod
    def get_name(cls):
        return 'Прямоугольник'

    def area(self):
        return self.height * self.width

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} имеет площадь {}'.format(self.get_name(), self.colour.colour_property,
                                                                             self.width, self.height,  self.area())

