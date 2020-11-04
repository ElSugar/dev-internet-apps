import random


# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    list_ans = [random.randint(begin, end) for _ in range(num_count)]
    # print(*list_ans, sep=', ')
    return list_ans


if __name__ == '__main__':
    print(*gen_random(5, 1, 3), sep=', ')  # должен выдать выдать 5 случайных чисел
    # в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
