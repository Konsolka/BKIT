from lab_python_oop.geom_figure import GeometricFigure
from lab_python_oop.color import Color
from math import pi

class Circle(GeometricFigure):
    FIGURE_TYPE='Circle'

    def __init__(self, radius, color):
        self.col = Color()
        self.col.set_x(color)
        self.rad = radius
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    def virtual_calculate_figure_square(self):
        return pi*(self.rad**2)
    def __repr__(self) -> str:
        return '{} | Color {} | Radius {} | Area {}'.format(
            Circle.get_figure_type(),
            self.col.get_x(),
            self.rad,
            round(self.virtual_calculate_figure_square(), 2)
        )