# LIST
# ------------------------------------------------------------------------

# List used to store multiple items in a single variable. Lists are one of 4
#  built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.


# 1. List তৈরি করা

names = ["Rahul", "Shuvo", "Dhrubo", "Sourov"]
print(names) # Output: ['Rahul', 'Shuvo', 'Dhrubo', 'Sourov']

#2. List Indexing.

print(names[0]) # Output: Rahul
print(names[1]) # Output: Shuvo
print(names[2]) # Output: Dhrubo
print(names[3]) # Output: Sourov

# list indexing start from 0 and end at n-1. n = total number of elements in the list.


# changing list item value

names[2]= "Noman"
names[3]= "Nafee"
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Nafee']

