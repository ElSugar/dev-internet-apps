class Colour:
    def __init__(self):
        self.colour = None

    @property
    def colour_property(self):
        """
        Get-аксессор
        """
        return self.colour

    @colour_property.setter
    def colour_property(self, input_colour):
        """
        Set-аксессор
        """
        self.colour = input_colour
