# <<<<<<<<<<<<<<<<<<<<< Lists, Tuples & Sets >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# List → Use when you need an ordered collection that can change (add, remove, sort) and can contain duplicates.

# Tuple → Use when you need an ordered collection that should never change (fixed data, like coordinates or records).

# Set → Use when you need a collection of unique values only, don’t care about order, and want to do fast membership checks or mathematical operations (union, intersection, difference).
# Collections, indexing, adding/removing, sorting, set operations

# <<<<<< Lists (Ordered, mutable) >>>>>>>>>>>
transitions=[100, 200, 300, 400, 200]
print(transitions[0])   # Indexing
transitions.append(300) # 300 added
transitions.remove(200) # removed 200 first entry
# transitions.sort()      # Sort ascending
print(transitions)

# <<<<<<<<<<< Tuples (Ordered, immutable (cannot change after creation)) >>>>>>>>
#  Use tuples when data should not change (like fixed account details).
account = ("Alice", "Savings", 500)
print(account[0])  # Alice
# account[0] = 700 # this will throw errors because tupleas are immutable

# <<<<<<<<<<<<<<<<<<<<<<<<<< Sets (Unordered, unique values only.) >>>>>>>>>>>>>>>>>>>>>>>>>>
# Sets are great for mathematical operations.
unique_set = {100, 200, 400, 300, 200}
print(unique_set) # {200, 100, 400, 300} - It will remove dupicate value itself

unique_set.add(600)
unique_set.remove(100)
print(unique_set) # {200, 300, 400, 600}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b)) # {1, 2, 3, 4, 5} - it will union both sets and remove the common value.
print(a.intersection(b)) # {3} - It will show common value from both sets.
print(a.difference(b)) # {1, 2} - It will give values from a sets which is not present in b set.
print(b.difference(a)) # {4, 5} - It will give values from b sets which is not present in a set.

