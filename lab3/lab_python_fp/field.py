def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        return_list = [item[key] for item in items for key in item if key in args]
        #print(*[item[key] for item in items for key in item if key in args], sep=', ')
    else:
        return_list = []
        for item in items:
            return_list.append({key: item[key] for key in args})
        #print(return_list)
    return return_list


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
     ]

    print(*field(goods, 'title'), sep=', ')  # должен выдавать 'Ковер', 'Диван для отдыха'
    print(*field(goods, 'title', 'price'), sep=', ')
    # должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
