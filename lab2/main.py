from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle


def main():
    number = 22
    figure = [Rectangle(number, number, 'синего'), Circle(number, 'зеленого'), Square(number, 'красного')]
    for _ in range(3):
        print(figure[_])


if __name__ == "__main__":
    main()