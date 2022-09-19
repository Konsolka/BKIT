from lab_python_oop.geom_figure import GeometricFigure
from lab_python_oop.color import Color

class Rectangle(GeometricFigure):
    FIGURE_TYPE='Rectangle'
    def __init__(self, width, height, color):
        self.w = width
        self.h = height
        self.col = Color()
        self.col.set_x(color)

    def virtual_calculate_figure_square(self):
        return self.w*self.h
    
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    
    def __repr__(self):
        return '{} | Color {} | Width {} | Height {} | Area {}'.format(
            self.get_figure_type(),
            self.col.get_x(),
            self.w,
            self.h,
            self.virtual_calculate_figure_square()
        )