def print_result(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        print('-'*50)
        print(func.__name__)
        print('-'*10)
        if isinstance(res, dict):
            for k, v in res.items():
                print(k, '=', v)
        elif isinstance(res, list):
            for i in res:
                print(i)
        else:
            print(res)
        return res
    return inner


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
    test_1()
    test_2()
    test_3()
    test_4()