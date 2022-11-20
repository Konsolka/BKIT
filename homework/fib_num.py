def fib_nums(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    print(type(fib_nums(1)))
    print(list(fib_nums(10)))