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
print (converted)

nuembers = [5, 12, 7, 12, 20, 5, 30, 7, 40, 20, 15]
duplicate_removed = []
[duplicate_removed.append(x) for x in nuembers if x not in duplicate_removed and x>10]
sort_duplicate = sorted(duplicate_removed)
print(sort_duplicate) # output : [12, 15, 20, 30, 40]

nuembers = [5, 12, 7, 12, 20, 5, 30, 7, 40, 20, 15]
duplicate_removed = []
[duplicate_removed.append(x) for x in nuembers if x>10]
sort_duplicate = sorted(dict.fromkeys(duplicate_removed))
print(sort_duplicate) # output : [12, 15, 20, 30, 40]

data = [
    [15, 5, 20, 15],
    [30, 10, 25, 20],
    [5, 35, 30, 40]
]

challange  = sorted(sorted(dict.fromkeys([x for nn in data for x in nn if x>10])))
print(challange) # output : [15, 20, 25, 30, 35, 40]