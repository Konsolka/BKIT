from ctypes import BigEndianStructure
import random


def gen_random(count, begin_num, end_num):
    """return a random generated number

    Args:
        count (int): amount of numbers
        begin_num (int): begin of random number
        end_num (int): end of random number

    Yields:
        int: random number
    """
    for i in range(0, count):
        # return random.randint(begin_num, end_num)
        yield random.randint(begin_num, end_num)

if __name__ == '__main__':
    gen_f = gen_random(5, 1, 3)
    for i in gen_f:
        print(i)