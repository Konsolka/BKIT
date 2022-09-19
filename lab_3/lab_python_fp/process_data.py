from enum import unique
import json
from logging import exception
from operator import contains
import sys
from cm_timer import cm_timer1
from gen_random import gen_random
from sort import sort_py
from unique import Unique
from unique import print_test
from print_result import print_result
from field import field

# Сделаем другие необходимые импорты

path = 'lab_python_fp/data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sort_py(list(Unique(field(data, 'job-name'), True)))

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

if __name__ == '__main__':
    with cm_timer1():
        f4(f3(f2(f1(data))))
