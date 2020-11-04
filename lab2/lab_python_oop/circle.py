from math import pi
from lab_python_oop.geometric_figure import Figure
from lab_python_oop.colour import Colour


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, input_colour, input_radius):
        self.radius = input_radius
        self.fc = Colour()
        self.fc.colour_property = input_colour

    def area(self):
        return pi*(self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colour_property,
            self.radius,
            self.area()
        )
