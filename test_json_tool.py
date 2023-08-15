import unittest
import json
import json_tool

class TestJsonTool(unittest.TestCase):

    def test_small_json(self):
        # Prepare a small json file
        data = {"key1": "value1", "key2": "value2"}
        with open('small.json', 'w') as file:
            json.dump(data, file)

        # Call the function with small.json
        keys = json_tool.print_json_keys('small.json')
        self.assertEqual(sorted(keys), sorted(data.keys()))

    def test_large_json(self):
        # Prepare a large json file
        data = {"key"+str(i): "value"+str(i) for i in range(100)}
        with open('large.json', 'w') as file:
            json.dump(data, file)

        # Call the function with large.json
        keys = json_tool.print_json_keys('large.json')
        self.assertEqual(sorted(keys), sorted(data.keys()))

if __name__ == '__main__':
    unittest.main()