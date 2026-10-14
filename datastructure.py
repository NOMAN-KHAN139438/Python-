# LIST
# ------------------------------------------------------------------------

# List used to store multiple items in a single variable. Lists are one of 4
#  built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.


# 1. List making

names = ["Rahul", "Shuvo", "Dhrubo", "Sourov"]
print(names) # Output: ['Rahul', 'Shuvo', 'Dhrubo', 'Sourov']

#-----------------------------------------------

#2. List Indexing.

#-----------------------------------------------

print(names[0]) # Output: Rahul
print(names[1]) # Output: Shuvo
print(names[2]) # Output: Dhrubo
print(names[3]) # Output: Sourov

# list indexing start from 0 and end at n-1. n = total number of elements in the list.

#-----------------------------------------------

# 3. Changing list item value

#-----------------------------------------------

names[2]= "Noman"
names[3]= "Nafee"
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Nafee']

#-----------------------------------------------

# 4. List methods

#-----------------------------------------------


#4.1 Append() method - a item will add at the end of the list.

names.append("Sabbir")
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Nafee', 'Sabbir']

#4.2 Insert() method - a item will add at the specific index of the list.

names.insert(3, "Tamim")
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Tamim', 'Nafee', 'Sabbir']

#4.3 Remove() method - a item will remove by using value from the list.
names.remove("Nafee")
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Tamim', 'Sabbir']

# 4.4 Pop () method - a item will remove by using index from the list.
names.pop(3)
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Sabbir']

# 4.5 sort () method - a item will sort the list in ascending order. (smaller to larger)
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)   # Output: [1, 2, 5, 7, 9]

numbers.sort(reverse=True)
print(numbers)   # Output: [9, 7, 5, 2, 1]

# 4.6 reverse () method - a item will reverse the order of the list.
names.reverse()
print(names)   # Output: ['Sabbir', 'Noman', 'Shuvo', 'Rahul']

# 4.7 clear () method - a item will remove all the items from the list.
numbers.clear()
print(numbers)   # Output: []

# 4.8 count () method - a item will count the number of occurrences of a specific value in the list.
number = [10, 20, 10, 30, 10, 40]
count = number.count(10)
print(count)   # Output: 3

# 4.9 index () method - a item will return the index of the first occurrence of a specific value in the list.
index = names.index("Shuvo")
print(index)   # Output: 2

# 4.10 copy () method - a item will create a shallow copy of the list.
names_copy = names.copy()
print(names_copy)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Sabbir']

# 4.11 extend () method - a item will add multiple items to the end of the list.
names.extend(["Rafi", "Rasel"])
print(names)   # Output: ['Rahul', 'Shuvo', 'Noman', 'Sabbir', 'Rafi', 'Rasel']

#-----------------------------------------------

# 5. LIST Slicing 

#-----------------------------------------------

# RULE   --------  ( Start : Stop : Step)

skills = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]

print(skills[2:4])  # Output: ['C++', 'JavaScript']

print(skills[::2])  # Output: ['Python', 'C++', 'HTML']

print(skills[1:5:2])  # Output: ['Java', 'JavaScript']

print(skills[1::2])  # Output: ['Java', 'JavaScript', 'CSS']

print(skills[:-5:-2])  # Output: ['CSS', 'JavaScript']

print(skills[1:-5:-1])  # Output: []

print(skills[:-5:-1])  # Output: ['CSS', 'HTML', 'JavaScript', 'C++']

# ------------------------------------------------------

# 6. List Looping

#-----------------------------------------------------

for skill in skills:
    print(skill) # Output:     Python
                              #Java
                              #C++
                              #JavaScript
                              #HTML
                              #CSS


for index, skill in enumerate(skills):
    print(index,".", skill) # Output: 0 . Python
                                     #1 . Java
                                     #2 . C++
                                     #3 . JavaScript
                                     #4 . HTML
                                     #5 . CSS


for index,  name in enumerate(names):
    print(index,".", name) # Output: 0 . Sabbir
                                    #1 . Noman
                                    #2 . Shuvo
                                    #3 . Rahul
                                    #4 . Rafi
                                    #5 . Rasel                                    


# -------------------------------------------------------------

# 7.  LIST COMPREHENSION

# -------------------------------------------------------------

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Structure: [expression for item in iterable if condition == True]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [x*x for x in numbers]
minus = [x-1 for x in numbers if x > 2]

print(square)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(minus)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# EVEN 
even = [x for x in numbers if x % 3 ==0]
print(even)   # Output: [3, 6, 9]

# ODD
odd = [x for x in numbers if x % 2 !=0]
print(odd)   # Output: [1, 3, 5, 7, 9]

# Bigger than 5
bigger = [x for x in numbers if x >5]
print(bigger)   # Output: [6, 7, 8, 9, 10]

# ----------------
# List comprehension with if else statement
# ----------------

# RULES: [expression_if_true if condition else expression_if_false for item in iterable]

even_odd = [f"{x} = Even" if x % 2 == 0 else f"{x} = Odd" for x in numbers]
print(even_odd)   # OUTPUT : ['1 = Odd', '2 = Even', '3 = Odd', '4 = Even', '5 = Odd', '6 = Even', '7 = Odd', '8 = Even', '9 = Odd', '10 = Even']

marks = [35, 75, 45, 90, 25, 60]
results = [f"{x} = Pass" if x>= 50 else f"{x} = Fail" for x in marks]
print(results)   # OUTPUT : ['35 = Fail', '75 = Pass', '45 = Fail', '90 = Pass', '25 = Fail', '60 = Pass']