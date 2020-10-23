from math import pi
from lab_python_oop.geometric_figure import Figure
from lab_python_oop.colour import Colour


class Circle(Figure):
    def __init__(self, input_radius, input_colour):
        self.radius = input_radius
        self.colour = Colour()
        self.colour.colour_property = input_colour

    @classmethod
    def get_name(cls):
        return 'Круг'

    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return '{} {} цвета радиусом {} имеет площадь {}'.format(self.get_name(), self.colour.colour_property,
                                                                 self.radius, self.area())
