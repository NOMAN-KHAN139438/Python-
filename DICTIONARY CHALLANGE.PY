# ============================================================
# PYTHON DICTIONARY PRACTICE
# LEVEL 5: ADVANCED CHALLENGES
# ============================================================

# RULES:
# 1. Solve every task independently.
# 2. Do not use collections.Counter.
# 3. Do not search for solutions.
# 4. Use loops, conditions, and dictionary methods.
# 5. Write clean and readable code.
# 6. Test your solutions with different inputs.


# ============================================================
# TASK 01: Find the Second Highest Value
# ============================================================

# Find the second highest unique value in the dictionary.
# Print the key and its corresponding value.

scores = {
    "Noman": 85,
    "Rahim": 95,
    "Karim": 92,
    "Sakib": 95,
    "Hasan": 78
}

# Expected output:
# Second highest value: 92
# Student: Karim


# Write your solution below:

unique_values = list(set(scores.values()))
unique_values.sort()
print(f"Second highest value : {unique_values[-2]}")          # Outpur : Second highest value : 92
for name, score in scores.items():
    if score == unique_values[-2]:
        print(f"Student : {name}")                            # Outpur : Student : Karim

# ============================================================
# TASK 02: Merge Dictionaries and Sum Duplicate Keys
# ============================================================

# Merge both dictionaries.
# If a key exists in both dictionaries, add their values.

dict1 = {
    "Python": 90,
    "SQL": 80,
    "Excel": 75
}

dict2 = {
    "Python": 85,
    "SQL": 90,
    "Power BI": 88
}

# Expected result:
# {
#     "Python": 175,
#     "SQL": 170,
#     "Excel": 75,
#     "Power BI": 88
# }


# Write your solution below:

result = dict1.copy()
for key , value in dict2.items():
    if key in result:
        result[key]+= value
print(result)

# ============================================================
# TASK 03: Find Common Keys and Different Values
# ============================================================

# Find keys that exist in both dictionaries.
# Print only the keys whose values are different.

employee1 = {
    "name": "Noman",
    "age": 24,
    "salary": 20000,
    "department": "IT"
}

employee2 = {
    "name": "Noman",
    "age": 25,
    "salary": 25000,
    "department": "IT"
}

# Expected output:
# {
#     "age": (24, 25),
#     "salary": (20000, 25000)
# }


# Write your solution below:

result = {}
for key , valuee in employee1.items():
    if key in employee2 and employee2[key]!= valuee:
        result[key] = (value, employee2[key])
print(result)

# ============================================================
# TASK 04: Group Words by Their First Character
# ============================================================

# Group all words according to their first character.
# Convert the first character to lowercase.

words = [
    "Apple",
    "Ant",
    "Banana",
    "Ball",
    "Cat",
    "Car",
    "Dog"
]

# Expected result:
# {
#     "a": ["Apple", "Ant"],
#     "b": ["Banana", "Ball"],
#     "c": ["Cat", "Car"],
#     "d": ["Dog"]
# }


# Write your solution below:

result = {}
for i in words:
    first_char = i[0].lower()
    if first_char not in result:
        result[first_char] = []
    result[first_char].append(i)

print(result)

# ============================================================
# TASK 05: Find the Most Frequent Value
# ============================================================

# Count the frequency of each value.
# Find the most frequently occurring value.
# Print the value and its frequency.

data = {
    "a": "Python",
    "b": "Java",
    "c": "Python",
    "d": "C++",
    "e": "Python",
    "f": "Java"
}

# Expected output:
# Most frequent value: Python
# Frequency: 3


# Write your solution below:



# ============================================================
# TASK 06: Sort Dictionary by Values
# ============================================================

# Sort the dictionary in descending order based on values.
# Create a new dictionary with the sorted results.

products = {
    "Laptop": 80000,
    "Mouse": 1200,
    "Keyboard": 3500,
    "Monitor": 25000,
    "Headphone": 5000
}

# Expected result:
# {
#     "Laptop": 80000,
#     "Monitor": 25000,
#     "Headphone": 5000,
#     "Keyboard": 3500,
#     "Mouse": 1200
# }


# Write your solution below:



# ============================================================
# TASK 07: Nested Dictionary Analysis
# ============================================================

# Find:
# 1. The employee with the highest salary.
# 2. The employee with the lowest salary.
# 3. The average salary.
# 4. Employees earning more than 30000.

employees = {
    "emp1": {"name": "Noman", "salary": 25000},
    "emp2": {"name": "Rahim", "salary": 45000},
    "emp3": {"name": "Karim", "salary": 35000},
    "emp4": {"name": "Hasan", "salary": 20000},
    "emp5": {"name": "Sakib", "salary": 50000}
}

# Write your solution below:



# ============================================================
# TASK 08: Inventory Management System
# ============================================================

# Requirements:
# 1. Calculate the total inventory value.
# 2. Find the most expensive product.
# 3. Find products with stock below 10.
# 4. Calculate the total number of available items.

inventory = {
    "Laptop": {"price": 80000, "stock": 5},
    "Mouse": {"price": 1200, "stock": 25},
    "Keyboard": {"price": 3500, "stock": 8},
    "Monitor": {"price": 25000, "stock": 12},
    "Headphone": {"price": 5000, "stock": 6}
}

# Write your solution below:



# ============================================================
# TASK 09: Dictionary Data Cleaning
# ============================================================

# Clean the following dictionary:
# 1. Remove keys with None values.
# 2. Remove keys with empty strings.
# 3. Remove keys with empty lists.
# 4. Keep all other values unchanged.

raw_data = {
    "name": "Noman",
    "age": 24,
    "email": "",
    "phone": None,
    "skills": ["Python", "SQL"],
    "projects": [],
    "country": "Bangladesh",
    "experience": 0
}

# Expected result:
# {
#     "name": "Noman",
#     "age": 24,
#     "skills": ["Python", "SQL"],
#     "country": "Bangladesh",
#     "experience": 0
# }


# Write your solution below:



# ============================================================
# TASK 10: Mini Project - Employee Management System
# ============================================================

# Build an employee management program.

employees = {
    "E001": {"name": "Noman", "department": "IT", "salary": 25000},
    "E002": {"name": "Rahim", "department": "HR", "salary": 30000},
    "E003": {"name": "Karim", "department": "IT", "salary": 40000}
}

# Requirements:
# 1. Display all employees.
# 2. Add a new employee.
# 3. Update an employee's salary.
# 4. Remove an employee.
# 5. Search for an employee using employee ID.
# 6. Group employees by department.
# 7. Find the employee with the highest salary.
# 8. Calculate the average salary.

# Bonus:
# Build a menu-driven program.
# Continue running until the user chooses Exit.


# Write your solution below:



# ============================================================
# END OF ADVANCED CHALLENGE
# ============================================================
