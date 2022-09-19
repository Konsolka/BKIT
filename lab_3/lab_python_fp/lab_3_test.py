import io
import contextlib
import json
import os
from operator import ge
from random import random
from unittest import TestCase, main
from field import field
from print_result import print_result
from unique import Unique
from gen_random import gen_random
from random import randint
from process_data import f4, f3, f2, f1

class fireld_test(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.goods = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green', 'shape': None},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
            {'title': None, 'price': None, 'color': None, 'shape': None},
            {'title': 'Стул', 'price': '2500', 'color': 'black', 'shape': 'round'}
            ]
    def test_default_case(self):
        goods1 = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
        ]
        key_word = 'title'
        gen_field = iter(field(goods1, key_word))
        for i in goods1:
            self.assertEqual(next(gen_field), i[key_word])
    def test_none_case(self):
        key_words = ('title', 'shape')
        gen_field = iter(field(self.goods, *key_words))
        eq = {key_words[0]:self.goods[0][key_words[0]]}
        self.assertEqual(next(gen_field), eq)
        eq = {key_words[0]: self.goods[1][key_words[0]]}
        self.assertEqual(next(gen_field), eq)
        eq = {key_words[0]:self.goods[3][key_words[0]], key_words[1]:self.goods[3][key_words[1]]}
        self.assertEqual(next(gen_field), eq)
    def test_none_size_case(self):
        key_words = ('title', 'shape')
        gen_field = list(field(self.goods, *key_words))
        self.assertEqual(len(gen_field), 3)
        key_words = 'shape'
        gen_field = list(field(self.goods, key_words))
        self.assertEqual(len(gen_field), 1)
    def test_not_existing_keys_case(self):
        key_words = 'kek'
        gen_field = list(field(self.goods, *key_words))
        self.assertEqual(len(gen_field), 0)
        key_words = ('kke', 'lel')
        gen_field = list(field(self.goods, *key_words))
        self.assertEqual(len(gen_field), 0)

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
    
class print_result_test(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
    
    def test_test_case(self):
        captured_out = io.StringIO()
        with contextlib.redirect_stdout(captured_out):
            a = test_1()
            b = test_2()
            c = test_3()
            d = test_4()
        captures_string = captured_out.getvalue()
        compare_string='test_1\n{}\ntest_2\n{}\ntest_3\n{}\ntest_4\n{}\n'.format('1', 'iu5', 'a = 1\nb = 2', '1\n2')
        self.assertEqual(captures_string, compare_string)
        self.assertEqual(a, 1)
        self.assertEqual(b, 'iu5')
        self.assertEqual(c, {'a': 1, 'b': 2})
        self.assertEqual(d, [1, 2])

class test_unique(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
    def test_list_int_case(self):
        data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        ret = list(Unique(data))
        self.assertEqual(ret, [1, 2])
    def test_random_case(self):
        for i in range(100):
            data = list(gen_random(randint(1, 20), randint(1, 20), randint(20, 100)))
            ret = sorted(list(Unique(data)))
            self.assertEqual(ret, sorted(list(set(data))))
    def test_list_str_ignore_false_case(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        ret = list(Unique(data))
        self.assertEqual(ret, ['a', 'A', 'b', 'B'])
    def test_list_str_ignore_true_case(self):
        data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
        ret = list(Unique(data, True))
        self.assertEqual(ret, ['a', 'b'])
    def test_list_int_str_ignore_true_case(self):
        data = [1, 2, 3, 4, 3, 's', 'S']
        ret = list(Unique(data, True))
        self.assertEqual(ret, [1, 2, 3, 4, 's'])
    def test_list_int_str_ignore_false_case(self):
        data = [1, 2, 3, 4, 3, 's', 'S']
        ret = list(Unique(data, False))
        self.assertEqual(ret, [1, 2, 3, 4, 's', 'S'])
    def test_list_str_dc_ignore_false_case(self):
        data = ['as', 'aS', 'Aa', 'AA', 'aA', 'aa', 5, 'aA']
        ret = list(Unique(data))
        self.assertEqual(ret, ['as', 'aS', 'Aa', 'AA', 'aA', 'aa', 5])
    def test_list_str_dc_ignore_true_case(self):
        data = ['as', 'aS', 'Aa', 'AA', 'aA', 'aa', 5, 'aA']
        ret = list(Unique(data, True))
        self.assertEqual(ret, ['as', 'aa', 5])

class process_data_test(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
    def test_simple_output_check(self):
        path = os.path.dirname(__file__) + '\data_light.json'
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        captured_out = io.StringIO()
        with contextlib.redirect_stdout(captured_out):
            ret = f4(f3(f2(f1(data))))
        self.assertEqual(len(ret), 9)

if __name__ == '__main__':
    main()