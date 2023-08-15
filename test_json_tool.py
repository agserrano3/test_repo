import unittest
import json
import json_tool

class TestJsonTool(unittest.TestCase):

    def test_small_json(self):
        # Prepare a small json file
        data = {"key1": "value1", "key2": {"nested_key1": "value2", "nested_key2": "value3"}}
        with open('small.json', 'w') as file:
            json.dump(data, file)

        # Call the function with small.json
        keys = json_tool.print_json_keys(data)
        self.assertEqual(sorted(keys), sorted(["key1", "key2", "key2.nested_key1", "key2.nested_key2"]))


    def test_large_json(self):
        # Prepare a large json file
        data = {"key"+str(i): "value"+str(i) for i in range(50)}
        data["nested"] = {"key"+str(i): "value"+str(i) for i in range(50, 100)}
        with open('large.json', 'w') as file:
            json.dump(data, file)

        # Call the function with large.json
        keys = json_tool.print_json_keys(data)
        expected_keys = [f"key{i}" for i in range(50)] + [f"nested.key{i}" for i in range(50, 100)]
        self.assertEqual(sorted(keys), sorted(expected_keys))

if __name__ == '__main__':
    unittest.main()