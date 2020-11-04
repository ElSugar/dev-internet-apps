from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle


def main():
    number = 22
    example_rectangle = Rectangle("красного", number, number - 1)
    example_square = Square("белого", number)
    example_circle = Circle("черного", number)
    print(example_rectangle)
    print(example_square)
    print(example_circle)


if __name__ == "__main__":
    main()
