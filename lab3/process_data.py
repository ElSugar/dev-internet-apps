import json
from github.lab3.lab_python_fp.cm_timer import cm_timer1
from github.lab3.lab_python_fp.field import field
from github.lab3.lab_python_fp.gen_random import gen_random
from github.lab3.lab_python_fp.print_result import print_result
from github.lab3.lab_python_fp.unique import Unique

path = 'data_light.json'

with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)


# Функция f1 должна вывести отсортированный список профессий без повторений
# (строки в разном регистре считать равными).
# Сортировка должна игнорировать регистр. Используйте наработки из предыдущих задач.


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))


# Функция f2 должна фильтровать входной массив и возвращать только те элементы,
# которые начинаются со слова “программист”. Для фильтрации используйте функцию filter.


@print_result
def f2(arg):
    return list(filter(lambda _: str(_).startswith('программист'), arg))


# Функция f3 должна модифицировать каждый элемент массива, добавив строку “с опытом Python”
# (все программисты должны быть знакомы с Python). Пример: Программист C# с опытом Python.
# Для модификации используйте функцию map.


@print_result
def f3(arg):
    return list(map(lambda _: str(_).title() + ' с опытом Python', arg))


# Функция f4 должна сгенерировать для каждой специальности зарплату от 100 000 до 200 000 рублей
# и присоединить её к названию специальности. Пример: Программист C# с опытом Python, зарплата 137287 руб.
# Используйте zip для обработки пары специальность — зарплата.


@print_result
def f4(arg):
    return dict(zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer1():
        f4(f3(f2(f1(data))))
