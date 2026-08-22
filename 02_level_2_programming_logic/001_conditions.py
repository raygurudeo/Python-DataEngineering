# <<<<<<<<<<<<<<<<<<< Concept: if / elif / else >>>>>>>>>>>>>>>

# Goal:
# Check data for:
# Missing IDs
# Invalid emails
# Negative salary
# Invalid age
# Missing city

customer = {
    "id": 101,
    "name": "Alice",
    "email": "alice@example.com",   # missing '@'
    "salary": 5000,
    "age": 30,
    "city": ""
}

if not customer.get("id"):
    print("Error: Missing ID")
elif "@" not in customer.get("email", ""):
    print("Error missing '@' ")
elif customer.get("salary", 0) < 0:
    print("Error: Salary can not be negative.")
elif customer.get("age", 0) < 18 or customer.get("age", 0) > 65:
    print("Error: Invalid age !")
elif not customer.get("city"):
    print("Error: Missing city")
else:
    print("Customer Data Is Valid !")

