# <<<<<<<<<<<<<<<<<<<<<<<<<<  Type Conversion in Python  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# String → Integer / Float :  Input from input() is always a string, so we often convert it
age_str="25"
print("Age: ", int(age_str)+5)

salary="10000.50"
print("Salary: ", float(salary)+10000)

# Integer / Float → String : Useful when combining numbers with text.
salary_int=10000
salary_str=str(salary_int)
print("Salary is " + salary_str)

# Integer → Float / Float → Integer 
years = 5
print("Years: ", float(years))

bonus=1000.80
print("Bonus: ", int(bonus))  # int() truncates decimals, it doesn’t round

# String → Boolean : Any non-empty string becomes True, empty string becomes False
status1="Hello"
status2=""
print(bool(status1), " ", bool(status2))

# Number → Boolean : Zero → False, non-zero → True
print(bool(0))
print(bool(100))
print(bool(100.10))

# Boolean → Integer / String
isEmployee=True
print(int(isEmployee))
print(str(isEmployee))

isIntern=False
print(int(isIntern))
print(str(isIntern))


# <<<<<<<<<<<<<<<<<<<<< input()  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# input() - Takes user input (always as string).
name = input("Enter a employee name: ")
age = int(input("Enter your age: "))     # it will take age input as string but convert to int
print("Employee Name : ",name, ", ", "Employee Age : ", age)
