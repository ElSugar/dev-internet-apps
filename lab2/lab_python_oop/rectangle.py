from lab_python_oop.geometric_figure import Figure
from lab_python_oop.colour import Colour


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, input_colour, input_width, input_height):
        self.width = input_width
        self.height = input_height
        self.fc = Colour()
        self.fc.colour_property = input_colour

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.colour_property,
            self.width,
            self.height,
            self.area()
        )
