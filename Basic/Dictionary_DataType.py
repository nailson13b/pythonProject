#Create a Dictionary
employeeData = {
    "name":"Anil",
    "number":123414214,
    "DOB":1992
}
print(employeeData)
print(employeeData)
print(type(employeeData))

# Access the value from dictionary
a = employeeData["number"]
print(a)

# Update or change the value
employeeData["name"] = "Kumar"
print(employeeData)

# Add Key and value for existing dictionary
employeeData["address"]="India"
print(employeeData)

# length of a dictionary
print(len(employeeData))

# Copy the dictionary to other variable
emp = employeeData.copy()
print(emp)

# Iterate both keys and values
for a,b in employeeData.items():
    print(a,b)

# Remove the value
employeeData.pop("address")
print(employeeData)

# Clear the dictionary
employeeData.clear()
print(employeeData)

# delete the dictionary
del employeeData