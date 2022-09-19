from typing import Any


def sort_py_abs(items:list[int]):
    return sorted(items, key=abs,  reverse=True)

def sort_py(items:list[Any]):
    return sorted(items)

sort_py_lambda = lambda x: sorted(x, key=abs, reverse=True)

if __name__=='__main__':
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    res = sort_py_abs(data)
    print(res)
    res_lambda = sort_py_lambda(data)
    print(res_lambda)
    data = ['d', 'a', 'c']
    res = sort_py(data)