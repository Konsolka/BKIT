from ftplib import CRLF
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

if __name__ == '__main__':
    crcl = Circle(24, 'Green')
    rect = Rectangle(48, 24, 'Blue')
    sq = Square(24, 'Red')
    a = np.arange(15).reshape(3, 5)
    print(crcl)
    print(rect)
    print(sq)
    print(a.shape)