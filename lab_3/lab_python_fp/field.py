def print_ans(lst:list[dict]):
    """format printing list

    Args:
        lst (list[dict]):
    """
    for item in lst:
        new_d = {x:item[x] for x in item.keys() if item[x] is not None}
        if len(new_d.items()) > 1:
            print(new_d)
        elif len(new_d.keys()) == 1:
            print(list(new_d.items())[0][1])

def field(items:list[dict], *args):
    """function for getting value by key

    Args:
        items (list[dict[str, Any]]):
    """
    assert len(args) > 0
    for item in items:
        if len(args) == 1 and item[args[0]] is not None:
            yield item[args[0]]
        elif len(args) > 1:
            d = {x:item[x] for x in args if x in item.keys() and item[x] is not None}
            if bool(d):
                yield d
        # new_lst.append({x:item[x] for x in keys if x in item.keys()})


from print_result import print_result

if __name__=='__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green', 'shape': None},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': None, 'price': None, 'color': None, 'shape': None},
    {'title': 'Стул', 'price': '2500', 'color': 'black', 'shape': 'round'}
    ]
    for g in field(goods, 'title', 'shape'):
        print(g)