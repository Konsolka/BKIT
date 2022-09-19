from enum import unique
import json
import os
from logging import exception
from operator import contains
from cm_timer import cm_timer1
from gen_random import gen_random
from sort import sort_py
from unique import Unique
from unique import print_test
from print_result import print_result
from field import field


@print_result
def f1(arg):
    return sort_py(list(Unique(field(arg, 'job-name'), True)))

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    zip_str = zip(arg, gen_random(len(arg), 100000, 200000))
    str_ans = ['{}, зарплата {} руб.'.format(a, b) for a,b in zip_str]
    return str_ans

def main():
    path = os.path.dirname(__file__) + '\data_light.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return f4(f3(f2(f1(data))))

if __name__ == '__main__':
    with cm_timer1():
        main()
