# JSON Module in Python
"""
The JSON (JavaScript Object Notation) module in Python provides an easy way to encode and decode 
data in JSON format.   
JSON is a lightweight data interchange format that is easy for humans to read and write, and easy 
for machines to parse and generate.   
The json module in Python allows you to convert Python objects into JSON strings and vice versa.

for strings
loads() -> to convert JSON string to Python object
dumps() -> to convert Python object to JSON string

for files
load() -> to read JSON data from a file and convert it to a Python object   
dump() -> to write a Python object as JSON data to a file
sorting keys in JSON output can be done using the 'sort_keys' parameter in the dumps() and dump() methods.
indentation can be added to JSON output using the 'indent' parameter which tell no of spaces in 
the dumps() and dump() methods.
"""
import json
# Example 1: Converting Python object to JSON string
python_dict = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(python_dict, indent=4, sort_keys=True)
print("JSON String:")
print(json_string)  

# Example 2: Converting JSON string to Python object
json_data = '{"name": "Bob", "age": 25, "city": "Los Angeles", "lonely": "null"}'
python_obj = json.loads(json_data)
print("\nPython Object:")
print(python_obj) 

# Example 3: Writing Python object to a JSON file
with open("data.json", "w") as json_file:
    json.dump(python_dict, json_file, indent=4, sort_keys=True)
    print("\nData written to data.json file.")

# Example 4: Reading JSON data from a file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print("\nData read from JSON file:")
    print(data) 
# -------------------------------------------------
# END OF PROGRAM
# -------------------------------------------------
