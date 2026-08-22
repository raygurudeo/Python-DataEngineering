#  <<<<<<<<<<<<<<<<<<<<<<<<<< Transations Analyzer project >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# below is the expected output from the given data.
# --- Transaction Report ---
# Transactions: [100, 200, 300, 200, 500, 100, 700]
# Total: 2100
# Unique Values: {100, 200, 300, 500, 700}
# Minimum: 100
# Maximum: 700
# Average: 300.0
# Duplicates: {100, 200}

transactions = [100, 200, 300, 200, 500, 100, 700]
print("-------- Transaction Report -----------")
print(f"Transactions: {transactions}")
print(f"Total: {sum(transactions)}")   #Total sum of numbers list
transactions_set = set(transactions)   #converting to sets to get unique value
print(f"Unique Values: {transactions_set}")
print(f"Minimum: {min(transactions)}") #Min value
print(f"Maximum: {max(transactions)}") #Max value
print(f"Average: {sum(transactions)/len(transactions)}") #Average value
duplicates = set([x for x in transactions if transactions.count(x) > 1]) #This is called list comprehension way to build a new list. first we have extracted the duplicates value using for loop it means the number which has count granter that 1 then converted that list into sets so that only unique valuse will show.
print("Duplicates: ", duplicates)

