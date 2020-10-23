class Colour:
    def __init__(self):
        self.hidden_colour = None

    @property
    def colour_property(self):
        return self.hidden_colour

    @colour_property.setter
    def colour_property(self, input_colour):
        self.hidden_colour = input_colour

