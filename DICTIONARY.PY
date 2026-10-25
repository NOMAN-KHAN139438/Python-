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
# 3. How to Access Dictionary Values
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


