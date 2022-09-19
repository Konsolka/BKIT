import sys
import argparse

from math import sqrt

def get_sqroot(root):
    '''
    Get square of root without errors
    Args:
        root(float)
    Returns:
        float/None
    '''
    if root < 0.0:
        return None
    else:
        return sqrt(root)

def get_roots(a, b, c):
    '''
    Calculating roots for equasion a*x^4+b*x^2+c=0

    Args:
        a(float): coeff of A
        b(float): coeff of B
        c(float): coeff of C

    Returns:
        list[float]: list of roots
    '''
    res = []
    d = b*b-4*a*c
    if d == 0.0:
        root = -b / (2*a)
        sqroot = get_sqroot(root)
        if sqroot is not None:
            res.append(sqroot)
            res.append(-sqroot)
    elif d > 0.0:
        sqd = sqrt(d)
        root1 = (-b-sqd)/(2*a)
        root2 = (-b+sqd)/(2*a)
        sqroot1 = get_sqroot(root1)
        sqroot2 = get_sqroot(root2)
        if sqroot1 is not None:
            res.append(sqroot1)
            res.append(-sqroot1)
        if sqroot2 is not None and sqroot2 != sqroot1:
            res.append(sqroot2)
            res.append(-sqroot2)
    res = list(map(lambda x: round(x, 2), res))
    return res

def parses_args():
    '''
    Parser arguments
    '''
    parser = argparse.ArgumentParser(description='Solves ax^4+bx^2+c=0 where a!= 0')
    parser.add_argument('num', nargs=3, type=float, help='Three int/float numbers ex: 1 3.5 -8.3')
    parser.parse_args()

def main():
    '''
    main function
    '''
    args = [float(x) for x in sys.argv[1:4]]
    ans = get_roots(args[0], args[1], args[2])
    len_ans = len(ans)
    if len_ans == 0:
        print('No roots')
    else:
        print('{} root '.format(len_ans), str(ans)[1:-1])
        

if __name__ == '__main__':
    parses_args()
    main()