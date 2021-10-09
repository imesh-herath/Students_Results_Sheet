#input
p = int(input('Please enter your credits at pass = '))
d = int(input('Please enter your credit at defer = '))
f = int(input('Please enter your credit at fail = '))

#making a tuple using marks
MARKS = (120, 100, 80, 60, 40, 20, 0)

#assigning the enterd user values to identify the result
if (p == MARKS[0] and d == MARKS[-1] and f == MARKS[-1]):
    print('Progress')

elif (p == MARKS[1] and (d in MARKS[-2:]) and (f in MARKS[-2:])):
    print('Progress (module trailer)')

elif ((p in MARKS[2:]) and (d in MARKS) and (f in MARKS[3:])):
    print('Do not Progress – module retriever')

elif ((p in MARKS[-3:]) and (d in MARKS[-3:]) and (f in MARKS[:3])):
    print('Exclude')