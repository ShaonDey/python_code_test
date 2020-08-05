from unittest import TestCase
import pytest
from utility import Utility
from node import Node


class TestUtility(TestCase):
    def test_find_least_common_ancestor_should_return_none_when_root_given_none(self):
        utility = Utility()
        mock_root = None

        actual_result = utility.find_least_common_ancestor(root=mock_root, node1=2, node2=3)

        assert actual_result is None

    def test_find_least_common_ancestor_should_return_root_when_same_root_and_node1_given(self):
        utility = Utility()
        mock_root = Node(1)
        mock_node1 = 1
        mock_node2 = 2

        actual_result = utility.find_least_common_ancestor(root=mock_root, node1=mock_node1, node2=mock_node2)

        assert actual_result.key == mock_root.key == mock_node1

    def test_find_least_common_ancestor_should_return_root_when_same_root_and_node2_given(self):
        utility = Utility()
        mock_root = Node(1)
        mock_node1 = 2
        mock_node2 = 1

        actual_result = utility.find_least_common_ancestor(root=mock_root, node1=mock_node1, node2=mock_node2)

        assert actual_result.key == mock_root.key == mock_node2

    def test_find_least_common_ancestor_should_return_same_node_when_given_nodes_are_same(self):
        utility = Utility()
        mock_node1 = 2
        mock_node2 = 3
        mock_root = Node(1)
        mock_root.left = Node(mock_node1)
        mock_root.right = Node(mock_node2)

        actual_result = utility.find_least_common_ancestor(root=mock_root, node1=mock_node1, node2=mock_node1)

        assert actual_result.key == mock_node1

    def test_find_least_common_ancestor_should_return_parent_node_when_given_nodes_are_on_different_branch(self):
        utility = Utility()
        mock_root_value = 1
        mock_node1 = 4
        mock_node2 = 7
        mock_root = Node(mock_root_value)
        mock_root.left = Node(2)
        mock_root.right = Node(3)
        mock_root.left.left = Node(mock_node1)
        mock_root.left.right = Node(5)
        mock_root.right.left = Node(6)
        mock_root.right.right = Node(mock_node2)

        actual_result = utility.find_least_common_ancestor(root=mock_root, node1=mock_node1, node2=mock_node2)

        assert actual_result.key == mock_root_value

    def test_find_least_common_ancestor_should_raise_runtime_error_when_exception_occurs(self):
        utility = Utility()
        mock_node1 = 2
        mock_node2 = 3
        mock_root = 1

        with self.assertRaises(RuntimeError) as context:
            utility.find_least_common_ancestor(root=mock_root, node1=mock_node1, node2=mock_node2)

        assert context.exception.args[0] == 'Oops! Something went wrong finding Least Common Ancestor.'
        assert type(context.exception.args[1]) == AttributeError


@pytest.mark.parametrize('mock_node1, mock_node2, expected_result', [[6, 7, 3], [3, 7, 3], [8, 7, 1]])
def test_find_least_common_ancestor_should_return_proper_result_when_given_nodes(mock_node1,
                                                                                 mock_node2,
                                                                                 expected_result):
    utility = Utility()
    mock_root = Node(1)
    mock_root.left = Node(2)
    mock_root.right = Node(3)
    mock_root.left.left = Node(4)
    mock_root.left.right = Node(5)
    mock_root.right.left = Node(6)
    mock_root.right.right = Node(7)
    mock_root.left.left.left = Node(8)
    mock_root.left.left.right = Node(9)

    actual_result = utility.find_least_common_ancestor(root=mock_root, node1=mock_node1, node2=mock_node2)

    assert actual_result.key == expected_result
