from abc import ABC, abstractmethod
from utility import Utility


class AbstractNestedData(ABC):

    def __init__(self, utility: Utility):
        self.utility = utility

    @abstractmethod
    def print_depth(self, data: dict):
        pass
