def print_result(func_to_decorate):

    def wrapped_func(*args, **kwargs):
        print(func_to_decorate.__name__)
        result = func_to_decorate(*args, **kwargs)
        if type(result) == dict:
            for key in result:
                # print('{} = {}'.format(key, result[key]))
                print('{}, зарплата {} руб.'.format(key, result[key]))
        elif type(result) == list:
            for value in result:
                print(value)
        else:
            print(result)
        return result

    return wrapped_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
