"""
-Storing the different data type values in order and list is changeable in run time. It allows duplicate values
-Values should assign to a variable in square brackets " [] "
    Ex : name_list = [1, "python", 2.3, 4]

"""
name_list = [1, "python", 2.3, 4, 5, 6, 7, 8, 9]
print(type(name_list))
print(name_list)

# Access the values in a list listName[indexValue]
a = name_list[1]
print(a)

a = name_list[-1]
print(a)

# Slicing - Getting the required portion of the values in the list [1:n-1].
b = name_list[1:5]

b = name_list[1:]
print(b)

# Update the value in the list append()

name_list.append("Python")
print(name_list)
# Inserting a value insert(index, "value")
name_list.insert(1, "World")
print(name_list)

# Remove the value from list
name_list.remove(9)
print(name_list)

# How to find the value in the list
a = "Python" in name_list
print(a)

# Iterate the list value
for a in name_list:
    print(a)

# Add two list items "+"
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# Delete the list
del name_list
print(name_list)

# Delete the list
