
"""
PROJECT: Python Sets - 50 Coding Challenges
AUTHOR: Noman
LEVEL: Beginner to Advanced
TOPIC: Python Data Structures

DESCRIPTION:
This project contains 50 coding challenges covering Python Sets.
Complete each task, test your code, and document your learning.

INSTRUCTIONS:
1. Read each question carefully.
2. Write your solution below the question.
3. Do not use external libraries.
4. Test your code before moving to the next task.
5. Commit your progress to GitHub regularly.
"""


# ============================================================
# SECTION 01: SET CREATION AND BASIC RULES
# ============================================================

# Task 01: Create a set containing the integers 10, 20, 30, 40, and 50.

number = {10, 20, 30, 40, 50}
print (number)   # Output : {50, 20, 40, 10, 30}

# Task 02: Convert the following list into a set to remove duplicates.
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]


numbers = [10, 20, 10, 30, 20, 40, 30, 50]
new_numbers = set(numbers)
print(new_numbers)        # Output : {40, 10, 50, 20, 30}


# Task 03: Create an empty set and an empty dictionary.
# Print the type of each object and explain the difference.

empty = {}
print(type(empty))  # Output: <class 'dict'>

empty_set = set()
print(type(empty_set))  # Output: <class 'set'>


# Task 04: Create a set containing an integer, a string, a float,
# and a Boolean value. Print the set and its type.


sst = {10, "Noman" , 30.22, True}
print(sst)           # Output: {True, 10, 30.22, 'Noman'}
print(type(sst))     # Output: <class 'set'>


# Task 05: Predict the output before running the code.
# data = {10, 20, 10, 30, 20, 40}
# print(len(data))
# Explain why the output has that value.

''' 
The output will be 4 because a set in Python only contains unique elements.

EXPLAINATION - A set in python only contains unique elements.. 
As we can in the set named data there are some duplicate object. So its physically looks like it has 6
elements. But when we chwck the length of the element id will return 4 beacause it only contains 4 elements.  '''

# ============================================================
# SECTION 02: ADDING ELEMENTS - add() AND update()
# ============================================================

# Task 06: Add the integer 40 to the following set using add().
# numberrs = {10, 20, 30}

numberrs = {10, 20, 30}
numberrs.add(40)
print(numberrs)  # Output: {10, 20, 30, 40}

# Task 07: Add the integer 20 to the following set.
# Print the set and its length. Explain why the length does
# not increase.
# numbers = {10, 20, 30}

nuuumbers = {10, 20, 30}
nuuumbers.add(20)
print(nuuumbers)             # Output: {10, 20, 30}
print(len(nuuumbers))        # Output: 3

"""EXPLAINATION - A set in python only contains unique elements.. 
As we can in the set named data there are some duplicate object. So its physically looks like it has 6
elements. But when we chwck the length of the element id will return 4 beacause it only contains 4 elements."""


# Task 08: Use update() to add all elements from new_numbers
# to numbers.
# numbers = {10, 20, 30}
# new_numbers = [30, 40, 50, 60]

nurmbers = {10, 20, 30}
new_numbers = [30, 40, 50, 60]
nurmbers.update(new_numbers)
print(nurmbers)                    # Output: {40, 10, 50, 20, 60, 30}

# Task 09: Use update() to add elements from both a list and
# a tuple to the same set.
# numbers = {1, 2}
# list_data = [3, 4, 5]
# tuple_data = (5, 6, 7)

nnnumbers = {1, 2}
list_data = [3, 4, 5]
tuple_data = (5, 6, 7) 
nnnumbers.update(list_data, tuple_data)
print(nnnumbers)            # Output:   {1, 2, 3, 4, 5, 6, 7}

# Task 10: Demonstrate the difference between add() and update().
# Use add() to insert one element and update() to insert multiple
# elements. Print the results and explain the difference.

num = {1, 2, 3, 4, 5, 6, 7}
num.add(22)
print(num)               # Output:    {1, 2, 3, 4, 5, 6, 7, 22}   
num.update([22,33])
print(num)                # Output:   {1, 2, 3, 4, 5, 6, 7, 22, 33}

'''
EXPLAINATION - add() in sets use for add one element in a set.
               update() in sets use for add more than one object.
               when we use update()  

'''


# ============================================================
# SECTION 03: REMOVING ELEMENTS
# remove(), discard(), pop(), AND clear()
# ============================================================

# Task 11: Remove the integer 30 using remove().
# numbers = {10, 20, 30, 40, 50}
numbersss = {10, 20, 30, 40, 50}
numbersss.remove(30)
print(numbersss) # output : {50, 20, 40, 10}

# Task 12: Attempt to remove the integer 100 from a set that
# does not contain it. Observe the exception.
# numbers = {10, 20, 30}

nuummbers = {10, 20, 30}
#nuummbers.remove(100)
#print(nuummbers)   # Output: KeyError: 100

# Task 13: Use discard() to remove the integer 100 from a set
# that does not contain it. Check whether an exception occurs.
# numbers = {10, 20, 30}

nnummbers = {10, 20, 30}
nnummbers.discard(100)
print(nnummbers)            # Output: {10, 20, 30}

# Task 14: Use pop() to remove one element from a set.
# Store the removed element in a variable.
# Print the removed element and the remaining set.
# Explain why you cannot predict which element will be removed.
# numbers = {10, 20, 30, 40}

nnumbeers = {10, 20, 30, 40}
nm = nnumbeers.pop()
print(nm)                # Output: 40
print(nnumbeers)         # Output: {10, 20, 30}
""" Explaination - Pop in set means it can remove any element from set .. and we cant decide to which one can be the removed ...  
thats why its un predictable wich elemet gonna removed.."""

# Task 15: Use clear() to remove every element from a set.
# Print the resulting set and its type.
# skills = {"Python", "AutoCAD", "3ds Max"}

skills = {"Python", "AutoCAD", "3ds Max"}
skills.clear()
print(skills)          # Output:   set()


# ============================================================
# SECTION 04: UNION
# ============================================================

# Task 16: Use union() to combine the following two sets.
# A = {10, 20, 30}
# B = {30, 40, 50}

A = {10, 20, 30}
B = {30, 40, 50}

print(A.union(B))         # Output:  {50, 20, 40, 10, 30}

# Task 17: Use the | operator to calculate the union.
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

D = {1, 2, 3, 4}
C = {3, 4, 5, 6}
print(C|D)         # Output:  {1, 2, 3, 4, 5, 6}

# Task 18: Combine three sets into one set containing all
# unique elements.
# A = {1, 2, 3}
# B = {3, 4, 5}
# C = {5, 6, 7}

Aa = {1, 2, 3}
Ab = {3, 4, 5}
Ac = {5, 6, 7}
print(Aa | Ab | Ac)           # Output :  {1, 2, 3, 4, 5, 6, 7}


#A Task 19: Find all students enrolled in at least one of
# the following courses.
python_students = {"Noman", "Rahim", "Sakib"}
java_students = {"Rahim", "Hasan", "Karim"}

print(python_students|java_students)         # Output :  {'Rahim', 'Sakib', 'Karim', 'Hasan', 'Noman'}

# Task 20: Calculate the union of A and B and store it in
# a new variable named result.
# Print A, B, and result to verify that the original sets
# remain unchanged.
# A = {10, 20, 30}
# B = {30, 40, 50}

A = {10, 20, 30}
B = {30, 40, 50}

result = A | B   
print (A) 
print (B) 
print (result)    # Output : {50, 20, 40, 10, 30}


# ============================================================
# SECTION 05: INTERSECTION
# ============================================================

# Task 21: Use intersection() to find the common elements.
# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(A.intersection(B))          # Output : {40, 30}

# Task 22: Use the & operator to find the intersection.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A&B)          # Output : {4, 5}


# Task 23: Find students who are enrolled in both Python
# and Java courses.
# python_students = {"Noman", "Rahim", "Sakib", "Rafi"}
# java_students = {"Rahim", "Sakib", "Hasan"}


python_students = {"Noman", "Rahim", "Sakib", "Rafi"}
java_students = {"Rahim", "Sakib", "Hasan"}

common_students = python_students & java_students
print(common_students)       # Output : {'Sakib', 'Rahim'}


# Task 24: Find the elements common to all three sets.
# A = {10, 20, 30, 40, 50}
# B = {20, 30, 40, 60}
# C = {20, 30, 70}

A = {10, 20, 30, 40, 50}
B = {20, 30, 40, 60}
C = {20, 30, 70}

print(A&B&C)        # Output : {20, 30}

# Task 25: Find the intersection of two sets with no common
# elements. Print the result and its type.
# A = {10, 20, 30}
# B = {40, 50, 60}


A = {10, 20, 30}
B = {40, 50, 60}
result = (A&B)              
print(result)          
print(type(result))            # Output: set()


# ============================================================
# SECTION 06: DIFFERENCE
# ============================================================

# Task 26: Find the elements present in A but not in B.
# A = {10, 20, 30, 40, 50}
# B = {30, 40, 50, 60, 70}


A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
print(A-B)               # Output: {10, 20}


# Task 27: Find the elements present in B but not in A.
# Use the same sets from Task 26.
# Explain why the result differs from A - B.

A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
print(B-A)               # Output: {60, 70}
"""Explaination - (B-A) means elements present in B but not in A. (A-B) means elements present in A but not in B"""

# Task 28: Use difference() to find programming languages
# present in A but not in B.
# A = {"Python", "Java", "C++", "JavaScript"}
# B = {"Java", "JavaScript"}

A = {"Python", "Java", "C++", "JavaScript"}
B = {"Java", "JavaScript"}
print(A.difference(B))               # Output:{'Python', 'C++'}



# Task 29: Find students who study Python but do not study Java.
# python_students = {"Noman", "Rahim", "Sakib", "Rafi"}
# java_students = {"Rahim", "Hasan", "Sakib"}

python_students = {"Noman", "Rahim", "Sakib", "Rafi"}
java_students = {"Rahim", "Hasan", "Sakib"}
print(python_students-java_students)               # Output:{'Rafi', 'Noman'}


# Task 30: Find the elements that remain in A after removing
# every element present in either B or C.
# A = {1, 2, 3, 4, 5, 6, 7}
# B = {2, 4, 6}
# C = {1, 3, 5}


A = {1, 2, 3, 4, 5, 6, 7}
B = {2, 4, 6}
C = {1, 3, 5}
print((A-B)-C)               # Output:{1, 3, 5, 7}

# ============================================================
# SECTION 07: SYMMETRIC DIFFERENCE
# ============================================================

# Task 31: Use symmetric_difference() to find elements that
# appear in exactly one of the two sets.
# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}


A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(A.symmetric_difference(B))               # Output:  {10, 50, 20, 60}


# Task 32: Solve Task 31 using the ^ operator.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A^B)               # Output:  {1, 2, 3, 6, 7, 8}


# Task 33: Find students who study either Python or Java,
# but not both.
# python_students = {"Noman", "Rahim", "Sakib"}
# java_students = {"Rahim", "Hasan", "Karim"}


python_students = {"Noman", "Rahim", "Sakib"}
java_students = {"Rahim", "Hasan", "Karim"}
print(python_students^java_students)               # Output:  {'Noman', 'Hasan', 'Karim', 'Sakib'}



# Task 34: Calculate the symmetric difference of A and B.
# Then calculate the symmetric difference of that result and C.
# A = {1, 2, 3}
# B = {2, 3, 4}
# C = {3, 4, 5}
# Check whether changing the grouping changes the result.


A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}
D = A^B
E= D^C

print(D)        # Output:  {1, 4}
print(E)        # Output:  {1, 3, 5}


# Task 35: Calculate both the union and symmetric difference
# of A and B. Explain which elements appear in both results
# and which elements appear only in the union.
# A = {10, 20, 30, 40}
# B = {30, 40, 50, 60}

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A^B)               # Output:  {10, 50, 20, 60}
print(A|B)               # Output:  {40, 10, 50, 20, 60, 30}

''' Explaination - {10, 50, 20, 60} those elements appear both in the symmetric difference & union. {30, 40} appeares only in union.'''



# ============================================================
# SECTION 08: SUBSET, SUPERSET, AND DISJOINT SETS
# ============================================================

# Task 36: Use issubset() to check whether A is a subset of B.
# A = {10, 20}
# B = {10, 20, 30, 40}


A = {10, 20}
B = {10, 20, 30, 40}
print(A.issubset(B))        # Output: True

# Task 37: Use issuperset() to check whether B is a superset of A.
# Use the same sets from Task 36.


A = {10, 20}
B = {10, 20, 30, 40}
print(B.issuperset(A))        # Output: True



# Task 38: Use isdisjoint() to check whether the sets have
# any common elements.
# A = {1, 2, 3}
# B = {4, 5, 6}


A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))       


# Task 39: Check all four relationships and print the results.
# A = {10, 20}
# B = {10, 20, 30}
# C = {10, 20, 30, 40}

A = {10, 20}
B = {10, 20, 30}
C = {10, 20, 30, 40}


# 1. Is A a subset of B?

print(A.issubset(B))                  # Output: True

# 2. Is B a subset of C?

print(B.issubset(C))                  # Output: True

# 3. Is C a superset of A?

print(C.issuperset(A))                # Output: True

# 4. Are A and C disjoint?

print(A.isdisjoint(C))                # Output: False


# Task 40: Compare the skill sets of three developers.
# noman_skills = {"Python", "SQL", "Git"}
# rahim_skills = {"Python", "SQL", "Git", "Docker"}
# sakib_skills = {"AutoCAD", "3ds Max"}

noman_skills = {"Python", "SQL", "Git"}
rahim_skills = {"Python", "SQL", "Git", "Docker"}
sakib_skills = {"AutoCAD", "3ds Max"}# Determine:

# 1. Whether Noman's skills are a subset of Rahim's skills.    # Output: True

print(noman_skills.issubset(rahim_skills))

# 2. Whether Rahim's skills are a superset of Noman's skills.      # Output: True

print(rahim_skills.issuperset(noman_skills))

# 3. Whether Noman's and Sakib's skill sets are disjoint.        # Output: True

print(noman_skills.isdisjoint(sakib_skills))


# ============================================================
# SECTION 09: DUPLICATE REMOVAL AND DATA PROCESSING
# ============================================================

# Task 41: Remove duplicates from the list using a set.
# numbers = [5, 10, 5, 15, 10, 20, 25, 20]

numbers = [5, 10, 5, 15, 10, 20, 25, 20]
print(list(set(numbers)))         # Output: [5, 10, 15, 20, 25]

# Task 42: Find the number of unique product IDs.
# product_ids = [
#     "A101", "A102", "A101",
#     "A103", "A102", "A104", "A103"
# ]

product_ids = [
    "A101", "A102", "A101",
    "A103", "A102", "A104", "A103"
] 
print(list(set(product_ids)))           # Output:      ['A104', 'A101', 'A102', 'A103']

# Task 43: Find products available on both websites.
# website_a = {"Fan", "Light", "Chair", "Table"}
# website_b = {"Chair", "Table", "Laptop", "Mouse"}

website_a = {"Fan", "Light", "Chair", "Table"}
website_b = {"Chair", "Table", "Laptop", "Mouse"}

print(website_a | website_b)           # Output:      {'Chair', 'Table', 'Light', 'Fan', 'Mouse', 'Laptop'}


# Task 44: Select numbers greater than 10 and remove duplicates.
# numbers = [5, 12, 7, 12, 20, 5, 30, 7, 40, 20, 15]

numbers = [5, 12, 7, 12, 20, 5, 30, 7, 40, 20, 15]
print(list(set(x for x in numbers if x>10)))            # Output: [40, 12, 15, 20, 30]

# Task 45: Remove duplicates while preserving the original order.
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]

numbers = [10, 20, 10, 30, 20, 40, 30, 50]
print(list(dict.fromkeys(numbers)))                 # Output:   [10, 20, 30, 40, 50]

# Do not use list(set(numbers)), because it does not guarantee
# preservation of the original order.


# ============================================================
# SECTION 10: LOOPS, SET COMPREHENSION, AND ADVANCED RULES
# ============================================================

# Task 46: Use a for loop to print every skill with the prefix
# "My Skill: ".
# skills = {"Python", "SQL", "Git", "Playwright"}

skills = {"Python", "SQL", "Git", "Playwright"}
for s in skills:
    print(s)               # Output:   Python
                                       #Playwright
                                       #SQL
                                       #Git


# Task 47: Use set comprehension to create a set containing
# only numbers greater than 20.
# numbers = [5, 10, 15, 20, 25, 30, 35, 40]

numbers = [5, 10, 15, 20, 25, 30, 35, 40]
n = {x for x in numbers if x>20}      
print(n)               # Output:    <generator object <genexpr> at 0x00000127F9596110>


# Task 48: Use set comprehension to create a set of squares
# of all even numbers from 1 through 10.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = {x*x for x in numbers if x%2 == 0}      
print(n)                             # Output:   <generator object <genexpr> at 0x00000127F9596180>
 

# Task 49: Explain and test the following expressions.
# numbers = {10, 20, 30}
numbers = {10, 20, 30}

# A. numbers[0]
#A = numbers[0]
# print(A)                           # Output:   TypeError: 'set' object is not subscriptable
# B. list(numbers)[0]
B = list(numbers)[0]
print(B)             # Output: 10


# Determine which expression raises an exception.
# Explain why the second expression's value is not guaranteed
# to be 10.

# Task 50: Complete a product price data-cleaning challenge.
# prices = [
#     1200, 1500, 1200, 2000, 1800,
#     1500, 2500, 3000, 2000, 3500,
#     1000, 2500, 4000
# ]

prices = [
    1200, 1500, 1200, 2000, 1800,
    1500, 2500, 3000, 2000, 3500,
    1000, 2500, 4000
]



# Requirements:
# 1. Remove duplicate prices using a set.
unique_prices = set(prices)
# 2. Select prices greater than or equal to 2000.
filter = []
[filter.append(x) for x in unique_prices if x >= 2000]
# 3. Ensure that the filtered result contains no duplicates.
result = []
[result.append(x) for x in filter if x not in result]
# 4. Print the set of all unique prices.
print(unique_prices)                             # Output: {4000, 2500, 1800, 1000, 3500, 1200, 2000, 3000, 1500}

# 5. Print the filtered set.
print(result)                                      # Output: [4000, 2500, 3500, 2000, 3000]

# 6. Print the number of filtered prices.
print(len(result))                                # Output: 5

# 7. Convert the filtered prices into a sorted list.
sorteed_list = sorted(result)

# 8. Print the sorted list.
print(sorteed_list)                               # Output:     None


# ============================================================
# END OF PROJECT
# ============================================================

#  Task 10, 20, 25, 30, 34, 35, 42, 43, 46, 47, 48, 49, 50।


