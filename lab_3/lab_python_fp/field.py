from ast import arg


def field(items:list[dict], *args):
    """function for getting value by key

    Args:
        items (list[dict[str, Any]]):
    """
    assert len(args) > 0
    for item in items:
        if len(args) == 1 and args[0] in item.keys() and item[args[0]] is not None:
            yield item[args[0]]
        elif len(args) > 1:
            d = {x:item[x] for x in args if x in item.keys() and item[x] is not None}
            if bool(d):
                yield d


if __name__=='__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green', 'shape': None},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': None, 'price': None, 'color': None, 'shape': None},
    {'title': 'Стул', 'price': '2500', 'color': 'black', 'shape': 'round'}
    ]
    k = 'shape'
    m = list(field(goods, k))
    for g in field(goods, k):
        print(g)