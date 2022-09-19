from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE='Square'
    
    def __init__(self, side, color):
        super().__init__(side, side, color)

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
    def __repr__(self):
        return super().__repr__()