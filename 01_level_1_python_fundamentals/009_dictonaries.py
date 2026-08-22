# <<<<<<<<<<<<<<<<<<<<<<<<<<<< Dictionaries >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Learn: Key/value data, nested structures, validation, JSON-style data
# Keys must be unique, values can repeat

# Use a dictionary when you need to store data with labels (keys) instead of just positions.
# Best for structured data where each item has multiple attributes (like customer ID, name, email).
# Perfect when you need fast lookups by a meaningful key (e.g., "email", "id") instead of index numbers.
# Useful for nested data (like JSON) where values themselves can be lists or other dictionaries.
# Choose dictionary when you want to validate fields (check if "email" exists) or map relationships (like product → price).

# Easy Comparison
# List → Ordered collection, good for sequences.
# Tuple → Ordered but fixed, good for records that never change.
# Set → Unique values only, good for membership checks.
# Dictionary → Key/value pairs, good for labeled, structured data.

# Real-world Examples
# Storing customer details → Dictionary ({"id": 101, "name": "Alice", "email": "alice@example.com"})
# Storing daily expenses → List ([200, 150, 300])
# Storing GPS coordinates → Tuple ((12.97, 77.59))
# Storing visited cities → Set ({"Delhi", "Mumbai", "Bangalore"})

# Get value using key
customer = {
    "id": 101,
    "name": "Guru"
}
print(f"ID: {customer["id"]}, Name: {customer["name"]}")

# Add new key/value or update existing
customer["email"] = "gdray1996@gmail.com"
customer["name"] = "Gurudeo Ray"
print(customer) # {'id': 101, 'name': 'Gurudeo Ray', 'email': 'gdray1996@gmail.com'}

# Delete keys or clear dictionary.
customer.pop("email")
print(customer) #{'id': 101, 'name': 'Gurudeo Ray'}
del customer["id"]
print(customer) #{'name': 'Gurudeo Ray'}
customer.clear()
print(customer) #{}

# Checking existence
customer = {
    "id": 101,
    "name": "Guru"
}
if "name" in customer:
    print("Exist")
else:
    print("Name does not exist")

# Looping
# Concept: Iterate through keys, values, or both.
for key in customer.keys():
    print(key) # 101

for value in customer.values():
    print(value) # Guru

for key, value in customer.items():
    print(f"Key: {key}, Value: {value}") # Key: name, Value: Guru

# Nested dictionaries
# Concept: Access inside another dictionary.
customer = {
    "id": 101,
    "address": {
        "city": "Bangalore",
        "zip": "560001"
    }
}
print(customer["address"]["city"]) #Bangalore

# Dictionary methods
# Concept: Built-in helpers.
print(customer.keys()) # dict_keys(['id', 'address'])
print(customer.values()) # dict_values([101, {'city': 'Bangalore', 'zip': '560001'}])
print(customer.items()) # dict_items([('id', 101), ('address', {'city': 'Bangalore', 'zip': '560001'})])

mail = {"email": "gurudeo.ray@iqvia.com"}
customer.update(mail)
print(customer) # {'id': 101, 'address': {'city': 'Bangalore', 'zip': '560001'}, 'email': 'gurudeo.ray@iqvia.com'}

# Validation
# Concept: Check required fields.
required = ["id", "name", "email"]
missing = [x for x in required if x not in customer]
print(f"Missing: {missing}")  # Missing: ['name']

# JSON operations
# Concept: Convert dictionary ↔ JSON string.
import json
customer_dict = {"id": 101, "name": "Alice"}
print(customer_dict) #{'id': 101, 'name': 'Alice'}
cust_json = json.dumps(customer_dict)      # json.dumps() : Disctonary -> Json (string)
print(cust_json) #{"id": 101, "name": "Alice"}

cust_dict = json.loads(cust_json) # json.loads() : JSON -> Dictonary
print(cust_dict) #{'id': 101, 'name': 'Alice'}



# Easy Notes
# Access → dict[key] or dict.get()
# Modify → dict[key] = value
# Remove → pop(), del, clear()
# Check → in
# Loop → keys(), values(), items()
# Nested → dict["outer"]["inner"]
# JSON → json.dumps() / json.loads()