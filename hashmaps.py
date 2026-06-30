d = {"name": "Alice", "age": 25, "city": "Paris"}

# Iterating over keys
for key in d:
    print(key, end=" ")  # Output: name age city
print('\n')
# Iterating over values
for value in d.values():
    print(value, end=" ")  # Output: Alice 25 Paris
print('\n')

# Iterating over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

print(d.items())
# Output:
# name: Alice
# age: 25
# city: Paris

d = {"name": "Alice", "age": 25, "city": "Paris"}

# keys() - Get all keys
print(d.keys())  # Output: dict_keys(['name', 'age', 'city'])

# values() - Get all values
print(d.values())  # Output: dict_values(['Alice', 25, 'Paris'])

# items() - Get all key-value pairs
print(d.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Paris')])

# copy() - Create a copy
d_copy = d.copy()
print(d_copy)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Paris'}

# update() - Merge another dictionary
d.update({"country": "France", "age": 26})
print(d)  # Output: {'name': 'Alice', 'age': 26, 'city': 'Paris', 'country': 'France'}

# setdefault() - Get value or set default
print(d.setdefault("gender", "Female"))  # Output: 'Female'
print(d)  # Output: {'name': 'Alice', 'age': 26, 'city': 'Paris', 'country': 'France', 'gender': 'Female'}

print(d.setdefault("age", "Female"))  # Output: 'Female'
