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
