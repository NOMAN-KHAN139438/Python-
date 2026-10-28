# =======================================
# 1. DEFINITION -  DICTIONARY 
# =======================================

student = {
    "name": "Noman",
    "age": 24,
    "department": "AI Engineering",
    "is_learning_python": True
}

print(student)

# OUTPUT :        {'name': 'Noman', 'age': 24, 'department': 'AI Engineering', 'is_learning_python': True}

"""
     DEFINITION - PYTHON dictionary is a kind of data structure type, where we can add and save data pair wise. 
"""

# =======================================
# 2. SYNDROM OF DICTIONARY 
# =======================================

"""| Rule | Explanation                                                                                              |
| ---- | -------------------------------------------------------------------------------------------------------- |
| 1    | Curly braces `{}` can be used to create a dictionary.                                                    |
| 2    | Data is stored in `Key: Value` pairs.                                                                    |
| 3    | Every key must be unique.                                                                                |
| 4    | Values can be duplicated.                                                                                |
| 5    | A dictionary is mutable, which means it can be modified.                                                 |
| 6    | Values can be accessed using their corresponding keys.                                                   |
| 7    | Strings, numbers, and suitable tuples can be used as dictionary keys.                                    |
| 8    | Various data types, including strings, integers, lists, sets, and dictionaries, can be stored as values. |
| 9    | Python dictionaries preserve insertion order.                                                            |
| 10   | Key-value pairs can be added, updated, and deleted in a dictionary.                                      |
"""

# =======================================
# 3. How to Create a Dictionary
# =======================================

#  3.1  USING CURLY BRACES

person = {
    "name": "Noman",
    "age": 24
}

print(person)    
# OUTPUT :       {'name': 'Noman', 'age': 24}

#  3.2 MAKING EMPTY DICTIONARY

person = {}

print(person)
# OUTPUT :       {}

#  3.3  BY USING DICT()

person = dict(name = "Noman", age = 24)
print(person)
# OUTPUT :       {'name': 'Noman', 'age': 24}

#  3.4 dictionary from list of tuples 

data = [
    ("name", "Noman"),
    ("age", 23),
    ("occupation", "Architect")
]

result = dict(data)
print(result)
# OUTPUT :     {'name': 'Noman', 'age': 23, 'occupation': 'Architect'}

# =======================================
# 4. How to Access Dictionary Values
# =======================================

# 4.1 by using square brecs []

student = {
    "name": "Noman",
    "age": 24,
    "department": "AI Engineering",
    "is_learning_python": True
}

print(student["name"])   # OUTPUT :         Noman
print(student["age"])    # OUTPUT :         24

#  4.2   get() method 

print(student.get("name"))                  # OUTPUT :         Noman
print(student.get("age"))                   # OUTPUT :         24
print(student.get("occupation"))            # OUTPUT :         none
print(student.get("hobby", "Not found"))    # OUTPUT :         Not found

"""
EXPLAINATION - this get("key") also return the value of a specific key like ["key"] method. but if there is no key with this specific name 
in ["key"] method the program would give us type error.. but the get(key") guves us none instead od error..  and we can decide which one reply 
would show if we get any erro.  like , (student.get("hobby", "Not found")) this one , we would get not found instead of none. 
"""

# =======================================
# 5. How to Add New Items
# =======================================

# 5.1 dictionary["key"]="Value"

student = {
    "name": "Noman",
    "age": 24
}

student["city"] ="Dhaka"
student["age"] = 44
print(student)        # Output : {'name': 'Noman', 'age': 44, 'city': 'Dhaka'}

""" 
Explaination - dictionary["key"] = "value" used for add new key and value.. and used for change the existing value..
"""

# 5.2 update()
student.update({
    "hobby": "Reading Books",
    "occupation": "Architect",
    "age": 23
})

print(student)          # Output :    {'name': 'Noman', 'age': 23, 'city': 'Dhaka', 'hobby': 'Reading Books', 'occupation': 'Architect'}

""" 
Explaination - dictionary.update({"key1": "value1", "key2": "value2"}) used for add multiple new key and value at once.. and used for change the existing value..
"""

# =======================================
# 6. How to dellete dictionary items  
# =======================================

# 6.1 pop()
student.pop("hobby")
print(student)                 # Output :       {'name': 'Noman', 'age': 23, 'city': 'Dhaka', 'occupation': 'Architect'}

# 6.2 del dictionary["key"]

del student["occupation"]
print(student)               # Output :   {'name': 'Noman', 'age': 23, 'city': 'Dhaka'}

# 6.3  dictionary.popitem() 
removed = student.popitem()
print(removed)                  # Output : ('city', 'Dhaka')
print(student)                  # Output : {'name': 'Noman', 'age': 23}

""" 
Explaination - dictionary.popitem() used for remove itrm.. it's removed last pair ofkey-value
"""
#  6.4  clear()
student.clear()
print(student)                   # Output :  {}


# =======================================
# 7. dictionary methods  
# =======================================

student = {
    "name": "Noman",
    "age": 24,
    "hobby": "Reading Books",
    "occupation": "Architect"
}

# 7.1 dictionary.keys()
print(student.keys())                                                      # Output :   dict_keys(['name', 'age', 'hobby', 'occupation'])

#7.2 dictionary.values()
print(student.values())                                                    # Output :   dict_values(['Noman', 24, 'Reading Books', 'Architect'])

# 7.3 dictionary.items()
print(student.items())                                                     # Output :   dict_items([('name', 'Noman'), ('age', 24), ('hobby', 'Reading Books'), ('occupation', 'Architect')])

#7.4 len(ditionary) 
print(len(student))                                                        # Output :   4

#7.5 operator :  key1 in dictionary output : true/ false

print("hobby" in student)             # used for check keys                # Output :     True
print("Architect" in student.values())  # used for check values            # Output :     True


# 7.6 dictionary.setdefault("key1", "default")

new = student.setdefault("city", "no home")
new_age = student.setdefault("age", "20+")
print(new_age)                     # Output :  24
print(new)                         # Output :  no home
print(student)                     # Output :  {'name': 'Noman', 'age': 24, 'hobby': 'Reading Books', 'occupation': 'Architect', 'city': 'no home'}


"""
Explination - if there is no key1 it returns with specific a default value. but if there is the key and its value it returns the oridinal value.. 
"""

#7.7 dictionary.copy()  - it's makes a shallow copy from another dictionary. 

copied = student.copy()
print(copied)                    # Output : {'name': 'Noman', 'age': 24, 'hobby': 'Reading Books', 'occupation': 'Architect', 'city': 'no home'}
 

# ==================================================
# 8.  Loop through a dictionary
# ==================================================

student = {
    "name": "Noman",
    "age": 24,
    "hobby": "Reading Books",
    "occupation": "Architect"
}

# 8.1  print only Key

for key in student:
    print(key)       # Output : name
                     # age
                     # hobby
                     # occupation

# 8.2  print only values
for value in student.values():
    print(value)     # Output : Noman
                     # 24
                     # Reading Books
                     # Architect


# 8.3 print both key and values 

for key, value in student.items():
    print(key, ":", value)            # Output   name : Noman
                                        #age : 24
                                        #hobby : Reading Books
                                        #occupation : Architect
                                        

students = {
    "Noman": 85,
    "Rahim": 72,
    "Karim": 91,
    "Sakib": 65,
    "Arjon": 33
}

for name, marks in students.items():
    if marks > 80: 
        print(f"Congratulations Mr. {name}. Yous got an A+. your mark {marks}")
    elif 80>marks>40 :
        print(f"Congratulation Mr. {name}. You passed. your mark {marks}")
    else:
        print(f"Sorry Mr. {name}. But, I'm afraid You are failed. your mark {marks}")

# -------------------------------------------------------------
# output:
# -------------------------------------------------------------
#  Congratulations Mr. Noman. Yous got an A+. your mark 85
#  Congratulation Mr. Rahim. You passed. your mark 72
#  Congratulations Mr. Karim. Yous got an A+. your mark 91
#  Congratulation Mr. Sakib. You passed. your mark 65
#  Sorry Mr. Arjon. But, I'm afraid You are failed. your mark 33
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

# -------------------------------------------------------------
# 9. Nested dictionary 
# -------------------------------------------------------------

students = {
    "student 1":{
        "name": "Noman",
        "Age": 24,
        "City": "Dhaka"
    },
    "student 2":{
        "name": "Rabby",
        "Age": 24,
        "City": "Pabna"
    } 
}

print(students)            # output: {'student 1': {'name': 'Noman', 'Age': 24, 'City': 'Dhaka'}, 'student 2': {'name': 'Rabby', 'Age': 24, 'City': 'Pabna'}}

print(students["student 2"]["name"])       # output: Rabby

students["student 3"] = {
        "name": "Rimon",
        "Age": 24,
        "City": "Pabna"
}

print(students["student 3"]["name"])    # output: Rimon

# -------------------------------------------------------------
# 10. Dictionary Comprehension 
# -------------------------------------------------------------

# {key_expression: value_expression for item in iterable}

# 10.1 square 

squares = {
    number: number ** 2
    for number in range(1, 6)  
}

print(squares)    # output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 10.2  square with condition

even_squares = {
    number: number ** 2
    for number in range(1, 11)  
    if number%2 == 0
}

print(even_squares)    # output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 10.3 List to dictionary
names = ["Noman", "Rahim", "Karim"]

name_length = {
    name : len(name) for name in names 
}

print(name_length)         # output:  {'Noman': 5, 'Rahim': 5, 'Karim': 5}

# 10.4 data filtering

students = {
    "Noman": 85,
    "Rahim": 55,
    "Karim": 92,
    "Sakib": 40
}

student_passed = {
    name: marks for name, marks in students.items()
    if marks>=80
    }

print(student_passed)       # output:  {'Noman': 85, 'Karim': 92}

# -------------------------------------------------------------
# 10. Dictionary unpacking   (adding two dictionary into one)
# ------------------------------------------------------------- 

first = {
    "name": "Noman",
    "age": 24
}

second = {
    "age": 25,
    "hobby": "Reading books"
}

combined = {
    **first,
    **second
}

print(combined)         # output:  {'name': 'Noman', 'age': 25, 'hobby': 'Reading books'}

# ------------------------------------------------------------- 
# 11. Dictionary to list
# ------------------------------------------------------------- 

student = {
    "name": "Noman",
    "age": 24,
    "score": 90
}

keys = list(student.keys())
print(keys)

values = list(student.values())
print(values)

items = list(student.items())
print(items)

