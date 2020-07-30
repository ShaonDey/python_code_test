from nested_dictionary import NestedDictionary
from person_dto import Person
from nested_object import NestedObject
from utility import Utility


utility = Utility()

# region for first solution

data_for_nested_dictionary = {
    'key1': 'val 1',
    'key2': {
        'key3': 'val 3',
        'key4': {
            'key5': 'val 5'
        }
    }
}
solution_for_nested_dictionary = NestedDictionary(utility=utility)

# endregion


# region for second solution

person_a = Person(first_name='User', last_name='One', father=None)
person_b = Person(first_name='User', last_name='Two', father=person_a)

data_for_nested_object = {
    'key1': 'val 1',
    'key2': {
        'key3': 'val 3',
        'key4': {
            'key5': 'val 5',
            'user': person_b
        }
    }
}

solution_for_nested_object = NestedObject(utility=utility)

# endregion


if __name__ == '__main__':
    solution_for_nested_dictionary.print_depth(data=data_for_nested_dictionary)
    solution_for_nested_object.print_depth(data=data_for_nested_object)
