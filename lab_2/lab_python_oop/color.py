class Color:
    def __init__(self):
        self._x = None
    def get_x(self):
        return self._x
    def set_x(self, val):
        self._x = val
    def del_x(self):
        del self._x
    
    x = property(get_x, set_x, del_x, 'Color')