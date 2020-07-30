from unittest import TestCase
from mock import Mock
from nested_object import NestedObject
from person_dto import Person


class TestNestedObject(TestCase):
    mock_utility = Mock()
    mock_nested_object: NestedObject = NestedObject(utility=mock_utility)
    mock_person_a: Person = Person(first_name='some one first', last_name='some one last', father=None)
    mock_person_b: Person = Person(first_name='some two first', last_name='some two last', father=mock_person_a)

    mock_raw_data = {
        'some key': 'some value',
        'some user': mock_person_b
    }
    mock_processed_data = {
        'some key': 'some value',
        'some user': 'some person'
    }

    def test_print_depth_should_call_utility_method_with_given_data(self):
        self.mock_utility.convert_data_to_dict = Mock(return_value=self.mock_processed_data)
        self.mock_utility.print_dict_key_level = Mock()

        self.mock_nested_object.print_depth(data=self.mock_raw_data)

        self.mock_utility.convert_data_to_dict.assert_called_once_with(raw_data=self.mock_raw_data)
        self.mock_utility.print_dict_key_level.assert_called_once_with(dict_data=self.mock_processed_data)

    def test_print_depth_when_exception_raised_from_utility_method(self):
        mock_utility = Mock()
        mock_exception = RuntimeError('Oops! Something went wrong.')
        mock_utility.convert_data_to_dict = Mock(side_effect=mock_exception)

        mock_nested_object: NestedObject = NestedObject(utility=mock_utility)

        mock_nested_object.print_depth(data=self.mock_raw_data)

        mock_utility.convert_data_to_dict.assert_called_once_with(raw_data=self.mock_raw_data)
        mock_utility.print_dict_key_level.assert_not_called()
