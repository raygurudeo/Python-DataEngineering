# <<<<<<<<<<<<<<<<<<<< Variables & Data Types >>>>>>>>>>>>>>>>>>>>>

# Variable = a name that stores a value in memory. 
# • In Python, you don’t declare types explicitly — the interpreter figures it out. 
# • Common data types: 
# o int → whole numbers (e.g., 10, -5) 
# o float → decimal numbers (e.g., 12.5, 0.99) 
# o str → text (e.g., "Alice") 
# o bool → True/False 
# o list → ordered collection (e.g., [1, 2, 3]) 
# o dict → key-value pairs (e.g., {"name": "Alice", "bill": 12000}) 

# Defining Patient data using variables and printing.
patient_id=101
patient_name="Gurudeo"
number_of_admission=3
total_bill=15000.50

print("Patient ", patient_id, " - ", patient_name, " - Admission: ",number_of_admission, " - Total Bill: ",total_bill );

# Variable/Data type checking
print("Type of patient ID: ", type(patient_id))
print("Type of Total Bill: ", type(total_bill))

# Dictionary Representation
# Store all patient details in a dictionary and print them
patient = {
    "patient_id":101,
    "patient_name":"Guru",
    "admission":3,
    "total_bill":15000.70
}
print("Patient record:", patient) #printing whole patient dictonary or data set
print("Patient Name: ", patient["patient_name"], " Patient Total Bill: ",patient["total_bill"])

# List : A list is an ordered collection of items.
# Lists can store multiple values in one variable. - my_list = [item1, item2, item3]
# You can access items by index (starting at 0)
# Lists are mutable → you can add, remove, or change elements.

# Practice Solution with patient IDs
patient_ids = [101, 102, 103]
print("First Patient ID:  ",patient_ids[0])

