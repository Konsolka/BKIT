from abc import ABC, abstractmethod
class GeometricFigure(ABC):
    @abstractmethod
    def virtual_calculate_figure_square(self):
        raise NotImplementedError('virtual_calculate_figure_square not implemented!')
