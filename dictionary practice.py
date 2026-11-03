# ============================================================
# PYTHON DICTIONARY PRACTICE
# Beginner to Advanced | Solve each task in your own code.
# Instructions:
# 1. Read each task carefully.
# 2. Write your solution below the task.
# 3. Do not look up solutions before trying yourself.
# 4. Run your file in VS Code and check your output.
# ============================================================


# ============================================================
# LEVEL 1: BEGINNER
# ============================================================

# Task 01: Create a Dictionary
# Create a dictionary named `student` with these key-value pairs:
#   name: "Noman"
#   age: 24
#   department: "AI Engineering"
#   is_learning_python: True
# Print the entire dictionary.


# Write your solution below:

student= {
    "name": "Noman",
    "age": 24,
    "department": "AI Engineering",
    "is_learning_python": True
}
print(student)              # output :    {'name': 'Noman', 'age': 24, 'department': 'AI Engineering', 'is_learning_python': True}



# Task 02: Access Dictionary Values
# Given the dictionary below, print the values of "name", "age",
# and "department" separately.
student = {
    "name": "Noman",
    "age": 24,
    "department": "AI Engineering"
}


# Write your solution below:

print(student["name"])             # Output : Noman
print(student["age"])              # Output : 24
print(student["department"])       # Output : AI Engineering

# Task 03: Add a New Key
# Add "country": "Bangladesh" to the dictionary below.
student = {
    "name": "Noman",
    "age": 24
}


# Write your solution below:
student["country"] = "Bangladesh" 
print(student)          # Output :       {'name': 'Noman', 'age': 24, 'country': 'Bangladesh'}


# Task 04: Update a Value
# Change the student's age from 24 to 25.
student = {
    "name": "Noman",
    "age": 24,
    "department": "AI Engineering"
}

student.update({
    "city": "Dahak"
})
# Write your solution below:
student.update({
    "city": "Dahak"
})
print(student)          # Output :  {'name': 'Noman', 'age': 24, 'department': 'AI Engineering', 'city': 'Dahak'}

# Task 05: Remove a Key
# Remove the "city" key from the dictionary below.
person = {
    "name": "Noman",
    "age": 24,
    "city": "Dhaka",
    "country": "Bangladesh"
}


# Write your solution below:

person.pop("city")
print(person)          # Output :  {'name': 'Noman', 'age': 24, 'country': 'Bangladesh'}

# ============================================================
# LEVEL 2: INTERMEDIATE
# ============================================================

# Task 06: Check Whether a Key Exists
# Check whether the key "email" exists in the dictionary.
# Print True if it exists; otherwise, print False.
student = {
    "name": "Noman",
    "age": 24,
    "department": "AI Engineering"
}
# Expected output:
# False


# Write your solution below:
print("email" in student)         # Output :  False


# Task 07: Use the get() Method
# 1. Get the employee's salary.
# 2. Get the employee's bonus, using 0 as the default if "bonus"
#    does not exist.
employee = {
    "name": "Noman",
    "position": "Junior Architect",
    "salary": 20000
}


# Write your solution below:
print(employee.get("salary"))        # Output :  20000
print(employee.get("bonus", 0))       # Output :  0


# Task 08: Loop Through a Dictionary
# Print each skill and its level in this format:
# Python : Beginner
# AutoCAD : Intermediate
# 3ds Max : Intermediate
# Playwright : Beginner
skills = {
    "Python": "Beginner",
    "AutoCAD": "Intermediate",
    "3ds Max": "Intermediate",
    "Playwright": "Beginner"
}


# Write your solution below:

for skill, level in skills.items():
    print(f"{skill} : {level}")

# Output :
#Python : Beginner
#AutoCAD : Intermediate
#3ds Max : Intermediate
#Playwright : Beginner

# Task 09: Count Dictionary Items Without len()
# Use a loop to count the number of key-value pairs.
# Do not use len().
data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}
# Expected output:
# Total items: 5


# Write your solution below:
count = 0 
for key in data:
    count += 1 
print(f"Total items: {count}")  # Output :  Total items: 5


# Task 10: Calculate Total and Average Marks
# Calculate and print:
# 1. The total marks.
# 2. The average marks.
marks = {
    "Bangla": 80,
    "English": 75,
    "Math": 90,
    "Science": 85
}


# Write your solution below:
total = 0 
for key, value in marks.items():
    total += value 
average = total / len( marks)    
print(total)                # Output : 330
print(average)              # Output : 82.5



# ============================================================
# LEVEL 3: PROBLEM SOLVING
# ============================================================

# Task 11: Find the Highest Value
# Find and print the subject with the highest marks and the marks.
marks = {
    "Bangla": 80,
    "English": 95,
    "Math": 88,
    "Science": 91
}
# Expected output:
# Highest subject: English
# Highest marks: 95


# Write your solution below:

for subject, mark in marks.items():
   if mark == max(marks.values()):
       print(f"Highest subject: {subject}")         # Output :      Highest subject: English
       print(f"Highest marks: {mark}")              # Output :     Highest marks: 95

# Task 12: Filter Dictionary Values
# Create a new dictionary containing only students who scored
# 80 or more. Do not modify the original dictionary.
students = {
    "Noman": 85,
    "Rahim": 65,
    "Karim": 92,
    "Sakib": 78,
    "Hasan": 88
}
# Expected result:
# {"Noman": 85, "Karim": 92, "Hasan": 88}


# Write your solution below:

for student, marks in students.items():
    if marks >= 80:
        print(f"{student}: {marks}")   
                            # Output : 
                            #Noman: 85
                            #Karim: 92
                            #Hasan: 88


# Task 13: Count Character Frequency
# Count how many times each character appears in the string.
# Do not use collections.Counter.
text = "banana"
# Expected result:
# {"b": 1, "a": 3, "n": 2}


# Write your solution below:
result = {}
for i in text:
    num = text.count(i)
    result[i] = num
print(result)  # Output : {'b': 1, 'a': 3, 'n': 2}

# Task 14: Merge Two Dictionaries
# Merge dict1 and dict2 into a new dictionary.
# Bonus: Try merging dictionaries that contain the same key.
dict1 = {
    "Python": 90,
    "SQL": 80
}
dict2 = {
    "Excel": 85,
    "Power BI": 88
}
# Expected result:
# {"Python": 90, "SQL": 80, "Excel": 85, "Power BI": 88}


# Write your solution below:

merged = {**dict1, **dict2}
print(merged)     #output : {'Python': 90, 'SQL': 80, 'Excel': 85, 'Power BI': 88}

# Task 15: Invert a Dictionary
# Create a new dictionary where each original value becomes a key
# and each original key becomes a value.
# Bonus: What happens if two original keys have the same value?
original = {
    "a": 1,
    "b": 2,
    "c": 3
}
# Expected result:
# {1: "a", 2: "b", 3: "c"}


# Write your solution below:

inverted = {}
for key, values in original.items():
    inverted[values] = key 
print(inverted)   # Output : {1: 'a', 2: 'b', 3: 'c'}


# ============================================================
# LEVEL 4: ADVANCED
# ============================================================

# Task 16: Count Duplicate Values
# Count how often each value appears.
# Return only values that appear more than once.
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}
# Expected result:
# {10: 2, 20: 2}


# Write your solution below:

result = {}
for value in data.values():
    num = list(data.values()).count(value)
    if num>1:
        result[value] = num
print(result)  # Output : {10: 2, 20: 2}


# Task 17: Work with a Nested Dictionary
# 1. Print Rahim's marks.
# 2. Print Noman's age.
# 3. Print every student's name.
# 4. Find the name of the student with the highest marks.
students = {
    "student1": {
        "name": "Noman",
        "age": 24,
        "marks": 85
    },
    "student2": {
        "name": "Rahim",
        "age": 22,
        "marks": 92
    },
    "student3": {
        "name": "Karim",
        "age": 23,
        "marks": 78
    }
}


# Write your solution below:

for student in students.values():
    if student["name"]=="Rahim":
        print(student["marks"])      # Output :   92
    
for student in students.values():
    if student["name"]=="Noman":
        print(student["age"])        # Output :   24
    print(student["name"])           # Output :   Noman
                                                # Rahim
                                                # Karim

highest = 0
topper = ""
for student in students.values():
    if student["marks"]>highest:
        highest = student["marks"]
        topper = student["name"]
print(highest)                       # Output :   92
print(topper)                        # Output :   Rahim



# Task 18: Group Students by Department
# Group the student names by department in a dictionary.
students = [
    {"name": "Noman", "department": "AI"},
    {"name": "Rahim", "department": "CSE"},
    {"name": "Karim", "department": "AI"},
    {"name": "Sakib", "department": "CSE"},
    {"name": "Hasan", "department": "Civil"}
]
# Expected result:
# {
#     "AI": ["Noman", "Karim"],
#     "CSE": ["Rahim", "Sakib"],
#     "Civil": ["Hasan"]
# }


# Write your solution below:

result = {}

for student in students:
    department = student["department"]
    name = student["name"]
    if department not in result:
        result[department] = []
    result[department].append(name)
print(result)
        

# Task 19: Update Store Inventory
# A customer buys:
#   2 laptops
#   5 mice
#   3 keyboards
# Update the inventory after the purchase.
# Bonus: If the requested quantity is greater than the stock,
# print "Insufficient stock" and do not allow the purchase.
inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}
# Expected result after the purchase:
# {"laptop": 8, "mouse": 20, "keyboard": 12}


# Write your solution below:

purchase = {
    "laptop": 2,
    "mouse": 2,
    "keyboard": 3
}

for item, quantity in purchase.items():
    inventory[item] -= quantity
print(inventory)                   # Output : {'laptop': 8, 'mouse': 23, 'keyboard': 12}

# BONUS 
# ___________

new = inventory

purchase = {
    "laptop": 2,
    "mouse": 2,
    "keyboard": 3
}

for item, quantity in purchase.items():
    if quantity> inventory[item]:
        print("Insufficient stock")
        break
else : 
        print(f"Purchase succesful. Now available: \n {inventory}")
# Output :
#Purchase succesful. Now available: 
# {'laptop': 8, 'mouse': 23, 'keyboard': 12}

# Task 20: Mini Project — Student Result Management System
# Start with the dictionary below and build a program that can:
# 1. Display all student names and marks.
# 2. Count the students.
# 3. Find the student with the highest marks.
# 4. Find the student with the lowest marks.
# 5. Calculate the average marks.
# 6. Display students who scored 80 or more.
# 7. Mark students who scored below 50 as "Fail".
# 8. Add a new student.
# 9. Update an existing student's marks.
# 10. Remove a student.
#
# Bonus: Make the program menu-driven so the user can choose
# actions repeatedly until they choose to exit.
students = {
    "Noman": 85,
    "Rahim": 67,
    "Karim": 92,
    "Sakib": 45,
    "Hasan": 78
}


# Write your solution below:

highest = 0
lowest = 0
num = 0
for name, marks in students.items():
    print(name, ":", marks)
    
    if marks > highest:
        highest = marks

    

    num+=1
count_student = num
print(highest)

print("Total Student: ",count_student)


for name, marks in students.items():
    if marks < lowest:
        lowest = marks

print(lowest)

num = 0
total = 0
for name, marks in students.items():

    total += marks
    num +=1
average = total/num
print(average)

passed = {name for name, marks in students.items() if marks>= 80 }
fail = {name for name, marks in students.items() if marks< 50 }
print(passed)
print(fail)

students["Pappu"] = 80


students.update({"Noman": 99})
students.pop("Sakib")

print(students)