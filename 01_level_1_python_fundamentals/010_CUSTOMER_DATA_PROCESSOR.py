# <<<<<<<<<<<<<<< Customer Data Processor Project >>>>>>>>>>>>>>>>>>>>
# Sample input : customer = {"id": 102, "name": "Bob", "active": False}
# Sample Output:
# {
#   "CustomerID": 102,
#   "Name": "Bob",
#   "Email": "N/A",
#   "Status": "Inactive",
#   "MissingFields": ["email"]
# }

# Goal:
# Validate required fields (id, name, email)
# Detect missing data
# Classify customers (Active / Inactive / Verified)
# Output in JSON-style format

import json
customer = {"id": 102, "name": "Bob", "active": False}

# Validate required fields (id, name, email)
validation = ["id","name","email"]
MissingFields = [x for x in validation if x not in customer.keys()] # Detect missing data

# Classify customers (Active / Inactive / Verified)
if customer.get("active", False) and "email" in customer: #checking if "active" field is there or not for a customer, if not default return False and checking if email field is there in customer.
    status = "Customer Verified"
elif customer.get("active", False): # if active field is there then return status as Active otherwise by default give status as False
    status = "Active"
else:
    status = "Inactive" # as customer has active field but status is False in list and also does not have email so status will be inactive

output = {  # formating output to a dictonary
    "CustetmerID": customer.get("id"),
    "Name": customer.get("name"),
    "Email": customer.get("email", "N/A"),
    "status": status,
    "MissingFields": MissingFields
}

print(json.dumps(output))  # Final output in Json






