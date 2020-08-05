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

    def find_least_common_ancestor(self, root, node1, node2):
        try:
            if root is None:
                return None

            if root.key == node1 or root.key == node2:
                return root

            left_lca = self.find_least_common_ancestor(root.left, node1, node2)
            right_lca = self.find_least_common_ancestor(root.right, node1, node2)

            if left_lca and right_lca:
                return root

            return left_lca if left_lca is not None else right_lca
        except Exception as exception:
            raise RuntimeError('Oops! Something went wrong finding Least Common Ancestor.', exception)
