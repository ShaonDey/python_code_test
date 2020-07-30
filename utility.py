import jsonpickle
import json


class Utility:

    @staticmethod
    def convert_data_to_dict(raw_data: object) -> dict:
        try:
            json_string = jsonpickle.encode(raw_data, unpicklable=False)
            processed_dict = json.loads(json_string)
            return processed_dict
        except Exception as exception:
            raise RuntimeError('Oops! Something went wrong in data conversion.', exception)

    def print_dict_key_level(self, dict_data: dict, depth: int = 0):
        try:
            depth += 1

            for key, value in dict_data.items():
                if isinstance(value, dict):
                    print(key, ':', depth)
                    self.print_dict_key_level(value, depth)
                else:
                    print(key, ':', depth)
        except Exception as exception:
            raise RuntimeError('Oops! Something went wrong in key level print.', exception)
