# <<<<<<<<<<<< Capstone Project (Employee Management System) >>>>>>>>>>>>>>>>>>>>>>

# What I will practice :
# Variables & Data Types → store employee info (ID, name, salary, age, city).
# Strings → clean and format names, emails, messages.
# Lists/Tuples/Sets → store transactions, departments, unique cities.
# Dictionaries → represent employees with key/value pairs.
# Conditionals (if/elif/else) → validate data (missing ID, invalid email, negative salary, invalid age).
# Loops (for/while) → process multiple employees in batch.

# Project Flow
# Input Employees: Each employee stored as a dictionary (id, name, email, salary, age, city).

# Validation:
# Missing ID → error
# Invalid email (no @) → error
# Negative salary → error
# Age < 18 or > 65 → error
# Missing city → error

# Classification:
# Active + valid email → Verified Employee
# Active only → Active Employee
# Inactive → Inactive Employee
# Summary Report:
# Total employees processed
# Count of valid vs invalid records
# Unique cities (using set)
# Average salary (using list)

employees = [
    {"id": 101, "name": "Alice", "email": "alice@example.com", "salary": 50000, "age": 30, "city": "Delhi", "active": True},
    {"id": None, "name": "Bob", "email": "bobexample.com", "salary": -2000, "age": 17, "city": "", "active": False},
    {"id": 103, "name": "Charlie", "email": "charlie@example.com", "salary": 40000, "age": 40, "city": "Mumbai", "active": True}
]

valid = 0
invalid = 0
total_employee = 0
unique_city = set()
salary = []
count = 0

while count < len(employees):
    if employees[count].get("active", False) and "@" in employees[count].get("email", ""):
        valid += 1
        total_employee += 1
        unique_city.add(employees[count].get("city",""))
    if employees[count].get("salary",0) > 0:
        salary.append(employees[count].get("salary"))
    elif employees[count].get("active", False):
        invalid += 1
        total_employee += 1
    else:
        invalid += 1
        total_employee += 1
    count += 1

print("----- Employee Report -------")
print(f"Total Employees: {total_employee}")
print(f"Valid Records: {valid}")
print(f"Invalid Records : {invalid}")
print(f"Unique Cities: {unique_city}")
print(f"Average Salary: {sum(salary)/len(salary)}")

