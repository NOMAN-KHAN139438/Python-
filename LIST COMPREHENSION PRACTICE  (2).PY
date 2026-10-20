double = [x*2 for x in range (1,10)]
print(double) # output : [2, 4, 6, 8, 10, 12, 14, 16, 18]

square = [x*x for x in range (1,10)]
print(square)  # output : [1, 4, 9, 16, 25, 36, 49, 64, 81]

names = ["noman", "rahim", "sakib", "karim"]
upper = [name.upper() for name in names]
print(upper)  # output : ['NOMAN', 'RAHIM', 'SAKIB', 'KARIM']

namess = ["Noman", "Rahim", "Sakib", "Rafi"]
first_letter = [name[0] for name in namess]
print(first_letter)  # output : ['N', 'R', 'S', 'R']

values = ["10", "20", "30", "40"]
covert_int = [ int(x) for x in values ]
print(covert_int)  # output : [10, 20, 30, 40]

nummbers = [12, 7, 20, 3, 15, 8, 25, 30]
even = [ x for x in nummbers if x%2 == 0 ]
print(even)  # output : [[12, 20, 8, 30]

nnumbers = [5, 12, 18, 3, 25, 9, 30]
bigger = [ x for x in nnumbers if x>10 ]
print(bigger)  # output : [12, 18, 25, 30]

marks = [35, 80, 45, 20, 90, 60]
pass_fail = [  f"{x} = pass" if x> 50 else f"{x} = Fail" for x in marks ]
print(pass_fail)  # output : ['35 = Fail', '80 = pass', '45 = Fail', '20 = Fail', '90 = pass', '60 = pass']

naames = ["Noman", "Ali", "Rahim", "Rafi", "Sakib"]
na = [ n for n in naames if len(n)>4]
print(na)   # output :  ['Noman', 'Rahim', 'Sakib']

umbers = [10, -5, 20, -3, 0, 8, -1]
replace = [ x   if x>0 else 0 for x in umbers ]
print(replace)  # output : [10, 0, 20, 0, 0, 8, 0]

nnm = [[1, 2], [3, 4], [5, 6]]
flatten  = [ x for nn in nnm for x in nn]
print(flatten)   # output : [1, 2, 3, 4, 5, 6]

nmm = [[1, 2, 2, 3], [4, 4, 5], [3, 6, 6]]
fllatten  = []
[ fllatten.append(x) for nn in nmm for x in nn if x not in fllatten]
print (fllatten)    # output : [1, 2, 3, 4, 5, 6]


nmv = [[5, 10, 15, 15], [20, 5, 25, 20], [30, 10, 35]]
fllaatten  = []
[ fllaatten.append(v) for nn in nmv for v in nn if v>10 and v not in fllaatten]
fllaatten.sort()
print (fllaatten)    # output : [15, 20, 25, 30, 35]

word = "comprehension"
vowel = ["a", "e", "i", "o", "u"]
extract = [ x for x in word if x in vowel ]
print (extract)    # output : ['o', 'e', 'e', 'i', 'o']

words = ["Python", "AI", "Automation", "Data"]
long_words = [len(word) for word in words ]
print (long_words)    # output : [6, 2, 10, 4]

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]
common = [x for x in a if x in b]
print(common)  # output : [4, 5, 6]

data = ["Noman", "", "Rahim", "", "Sakib", ""]
empty_removed = [ x for x in data if x!= ""]
print(empty_removed)  # output : ['Noman', 'Rahim', 'Sakib']

prices = ["৳500", "N/A", "৳1,200", "", "৳800", "Unknown"]
converted = [int(price.replace("৳", "").replace(",",""))for price in prices if price is not None and price != "" and price != "N/A" and price != "Unknown"]
print (converted)  # output : [500, 1200, 800]

nuembers = [15, 5, 20, 10, 15, 30, 5]

# 1. Add 25
# 2. Remove one 15
# 3. Sort in ascending order
# 4. Count how many times 5 appears
# 5. Use a loop to print every number

nuembers.append(25)
nuembers.pop(0)
nuembers.sort()
nuembers_count = nuembers.count(5)
for n in nuembers:
    print(n)






# ============================================================
# ADVANCED PYTHON LIST COMPREHENSION — 5 HARD CHALLENGES
# ============================================================


# CHALLENGE 1: Flatten + Filter + Transform + Unique + Sort
#
# Input:
data = [
    [12, 5, 20, 12],
    [30, 7, 25, 20],
    [5, 35, 30, 40],
    [45, 10, 25, 50]
]
#
# Tasks:
# 1. Flatten the nested list.
# 2. Keep only numbers greater than 15.
# 3. Keep only numbers divisible by 5.
# 4. Square each remaining number.
# 5. Remove duplicates.
# 6. Sort in descending order.

dat= sorted(dict.fromkeys([x*x for nn in data for x in nn if x>5 and x%5==0]), reverse=True)
print(dat)         #  Output:[2500, 2025, 1600, 1225, 900, 625, 400, 100]


# ============================================================
# CHALLENGE 2: String Processing + Multiple Conditions
#
# Input:
words = [
    "Python", "automation", "AI", "developer",
    "Data", "engineering", "Python", "agent",
    "machine", "learning", "AI", "system"
]

wrd= sorted(dict.fromkeys([word.lower()for word in words if len(word)>=5 and word[0].lower() not in "aeiou"]))
print(wrd)   # Output:   ['developer', 'learning', 'machine', 'python', 'system']



# Tasks:
# 1. Keep words containing at least 5 characters.
# 2. Exclude words starting with a vowel (a, e, i, o, u),
#    ignoring case.
# 3. Convert the remaining words to lowercase.
# 4. Remove duplicates.
# 5. Sort alphabetically.
#



# ============================================================
# CHALLENGE 3: Matrix Processing + Conditional Transformation
#
# Input:
matrix = [
    [2, 7, 12, 15],
    [8, 10, 21, 24],
    [5, 16, 30, 35],
    [18, 25, 32, 40]
]
#
# Tasks:
# 1. Flatten the matrix.
# 2. Keep only even numbers.
# 3. If a number is divisible by 4, divide it by 2.
#    Otherwise, multiply it by 3.
# 4. Keep only transformed values greater than 10.
# 5. Remove duplicates and sort in ascending order.


mat = sorted(dict.fromkeys([x//2 for mt in matrix for x in mt if x%4 == 0 and x//2 >10] + [x*3 for mt in matrix for x in mt if x%4 != 0 and x*3 > 10] ))
print(mat)               # Output:     # [[12, 15, 16, 20, 21, 30, 45, 54, 63, 75, 90, 105]]


# ============================================================
# CHALLENGE 4: Generate Unique Pairs with Constraints
#
# Input:
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
#
# Tasks:
# 1. Generate all possible ordered pairs (a, b).
# 2. a and b must be different.
# 3. a + b must equal 12.
# 4. a * b must be greater than 20.
# 5. Keep only pairs where a < b.
# 6. Sort pairs by their first element in ascending order.
#
# Constraint:
# Use a single List Comprehension with two for clauses.



pairs = sorted([(a,b) for a in numbers for b in numbers if a!=b and a<b and a*b>20 and a+b == 12])
print(pairs)        # Output:        [(3, 9), (4, 8), (5, 7)]


# ============================================================
# CHALLENGE 5: Advanced Data Cleaning Pipeline
#
# Each record contains: [name, age, skill, score]
#
# Input:
records = [
    [" Noman ", 25, "Python", 85],
    ["Rahim", 17, "Java", 72],
    ["Noman", 25, "Python", 85],
    ["Sakib", 22, "python", 90],
    ["  Nadia", 19, "SQL ", 65],
    ["Rahim ", 17, "Java", 72],
    ["Mim", 16, "HTML", 88],
    ["Sakib", 22, "Python ", 90],
    ["Rafi", 28, "AI", 95]
]
#
# Tasks:
# 1. Remove extra spaces from names and skills.
# 2. Convert all skills to lowercase.
# 3. Keep records where age >= 18 and score >= 80.
# 4. Remove duplicate records after cleaning.
# 5. Sort records by score in descending order.
# 6. Return only the name and skill as tuples: (name, skill).
#


rec = sorted(dict.fromkeys([(name.lower().strip(), skill.lower().strip())for name, age, skill, score in records if age >= 18 and score >= 80]),  reverse=True)
print(rec)   


# Constraint:
# Try to solve this using one List Comprehension.
# You may use sorted() and set() if needed, but preserve
# the required order.
#
# Expected Output:
# [
#     ('Rafi', 'ai'),
#     ('Sakib', 'python'),
#     ('Noman', 'python')
# ]


# ============================================================
# RULES:
# 1. Solve each challenge independently.
# 2. Use List Comprehension wherever possible.
# 3. Avoid regular for loops outside comprehensions.
# 4. Test your output against the expected output.
# 5. Do not look up solutions before attempting each challenge.
# ============================================================
