from gen_random import gen_random

class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.c = 0
        self.ignore_case=ignore_case
        self.items = self.get_unique(items, ignore_case)


    def get_unique(self, items, ignore_case):
        un = set()
        lst=[]
        if items is None:
            return
        for x in items:
            if isinstance(x, str):
                if ignore_case:
                    x = x.lower()
                if x not in un:
                    un.add(x)
                    lst.append(x)
            elif not isinstance(x, str) and x not in un:
                un.add(x)
                lst.append(x)
        return lst

    def __next__(self):
        if self.c < len(self.items):
            x = self.items[self.c]
            self.c += 1
            return x
        else:
            raise StopIteration
    def __iter__(self):
        return self

def print_test(test):
    print('-'*50)
    for i in test:
        print(i)

import os

if __name__ == '__main__':
    data =[1,3,4,3, 'S', True]
    test = Unique(data)
    print_test(test)
    data = gen_random(10, 1, 3)
    test = Unique(data)
    print_test(test)
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    test = Unique(data, True)
    data = ['as', 'aS', 'Aa', 'AA', 'aA', 'aa', 5]
    test = Unique(data, True)
    print_test(test)