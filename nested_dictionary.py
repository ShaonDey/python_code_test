from abstract_nested_data import AbstractNestedData
from utility import Utility


class NestedDictionary(AbstractNestedData):

    def __init__(self, utility: Utility):
        super().__init__(utility=utility)

    def print_depth(self, data: dict):
        try:
            print('Solution for nested dictionary')
            self.utility.print_dict_key_level(dict_data=data)
        except Exception as exception:
            print(exception.args[0])
        finally:
            print('\n')
