# Employee Data Calculator

# Collect employee details
employee_id=int(input("Please enter your employee ID: "))
employee_name=input("Enter your name: ")
basic_salary=float(input("Enter your basic salary: "))
bonus=float(input("Enter your bonus amount: "))
tax_rate=float(input("Enter your tax rate (e.g. : 0.2 for 20%): "))

# calculate gross salary, tax, and net salary
gross_salary = basic_salary + bonus
tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount

# Convert numbers to strings when printing with text
print("---- Employee salary details -------")
print("ID: ", employee_id)
print("Name: ", employee_name)
print("Gross Salary: ", gross_salary)
print("Tax Amount: ", tax_amount)
print("Net salary: ", net_salary)

