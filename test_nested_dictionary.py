from unittest import TestCase
from mock import Mock
from nested_dictionary import NestedDictionary


class TestNestedDictionary(TestCase):
    mock_utility = Mock()
    mock_nested_dictionary = NestedDictionary(utility=mock_utility)

    mock_raw_data = {
        'some key': 'some value'
    }

    def test_print_depth_should_call_utility_method_with_given_data(self):
        self.mock_utility.print_dict_key_level = Mock()

        self.mock_nested_dictionary.print_depth(data=self.mock_raw_data)

        self.mock_utility.print_dict_key_level.assert_called_once_with(dict_data=self.mock_raw_data)

    def test_print_depth_when_exception_raised_from_utility_method(self):
        mock_exception = RuntimeError('Oops! Something went wrong.')
        self.mock_utility.print_dict_key_level = Mock(side_effect=mock_exception)

        self.mock_nested_dictionary.print_depth(data=self.mock_raw_data)

        self.mock_utility.print_dict_key_level.assert_called_once_with(dict_data=self.mock_raw_data)
