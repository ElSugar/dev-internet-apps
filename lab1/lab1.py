import sys


def sign_coefficient(digit):
    if digit >= 0:
        return '+ ' + str(digit)
    else:
        return '- ' + str((-1) * digit)


def print_ans(str_ans):
    for i in range(len(str_ans)):
        print('x{0} = {1}'.format(i+1, str_ans[i]))


def calculate_ans(a, b, c):
    ans_t, ans_x = [], []
    print('%d*x^4 %s*x^2 %s' % (a, sign_coefficient(b), sign_coefficient(c)))
    discriminant = b ** 2 - 4 * a * c
    print('D = %d' % discriminant)
    if discriminant > 0:
        t = (-b - discriminant ** 0.5) / (2 * a)
        if t >= 0:
            ans_t.append(t)
        t = (-b + discriminant ** 0.5) / (2 * a)
        if t >= 0:
            ans_t.append(t)
        if len(ans_t) > 0:
            for i in range(len(ans_t)):
                if ans_t[i] != 0:
                    ans_x.append(ans_t[i] ** 0.5)
                    ans_x.append((-1) * ans_t[i] ** 0.5)
                else:
                    ans_x.append(ans_t[i] ** 0.5)
            print_ans(ans_x)
        else:
            print('Решения нет')
    elif discriminant == 0:
        t = (-b) / (2 * a)
        if t > 0:
            ans_x.append(t ** 0.5)
            ans_x.append((-1) * t ** 0.5)
            print_ans(ans_x)
        elif t == 0:
            ans_x.append(0)
            print_ans(ans_x)
        else:
            print('Решения нет')
    else:
        print('Решения нет')


print('Сахарова Елизавета Константиновна ИУ5-52Б')
if len(sys.argv) == 4 and sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[3].isdigit() and float(sys.argv[1]) != 0:
    calculate_ans(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
elif len(sys.argv) == 1:
    coefficients = []
    for _ in range(3):
        str_digit = input()
        while not str_digit.lstrip('-').isdigit() or (float(str_digit) == 0 and len(coefficients) == 0):
            print('Неверный ввод данных, попробуйте снова')
            str_digit = input()
        coefficients.append(float(str_digit))
    calculate_ans(coefficients[0], coefficients[1], coefficients[2])
else:
    print('Неверный ввод параметров, запустите программу еще раз')
