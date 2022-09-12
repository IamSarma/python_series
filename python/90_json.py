import json

# Reading JSON with the loads() function
# loads() stands for load string and not loads
string_of_json_data = '{"name": "Zophie","is_cat": true, "mice_caught": 0}'
json_to_python_value = json.loads(string_of_json_data)
print(json_to_python_value)
