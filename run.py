from nested_dictionary import NestedDictionary
from person_dto import Person
from nested_object import NestedObject
from utility import Utility
from node import Node

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


# region for third solution

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)


def lca(node1, node2):
    lca_node = utility.find_least_common_ancestor(root=root, node1=node1, node2=node2)
    print('LCA of ', node1, ' and ', node2, ' is ', lca_node.key)

# endregion


if __name__ == '__main__':
    solution_for_nested_dictionary.print_depth(data=data_for_nested_dictionary)

    solution_for_nested_object.print_depth(data=data_for_nested_object)

    lca(node1=6, node2=7)
    lca(node1=3, node2=7)
