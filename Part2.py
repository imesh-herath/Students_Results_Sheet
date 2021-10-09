#Getting varriables
p, d, f = 0, 0, 0

#Make a tuple using the marks
MARKS = (120, 100, 80, 60, 40, 20, 0)

#Checking the integers and the range of pass, defer, fail situations
def get_marks(situation):
    try:
        mark = int(input(f'Please enter your credits at {situation} = ').strip())
        if mark in MARKS:                    #checking the user input mark are availiable in the MARKS tuple
            return mark
        return 'Out of range.\n'
    
    except Exception as e:
        return 'Integer required\n'

while True:      
    while True:
            
        p, d, f = 0, 0, 0
            
        while True:
            mpass = get_marks('pass')
            if isinstance(mpass, int):              #checking the credits at pass is a integer
                p = mpass                           #if mpass is a integer it will assign to p
                break
            else:
                print(mpass)                        #othervise mpass will be looping
                    
        while True:
            mdefer = get_marks('defer')
            if isinstance(mdefer, int):
                d = mdefer
                break
            else:
                print(mdefer)

        while True:
            mfail = get_marks('fail')
            if isinstance(mfail, int):
                f = mfail
                break
            else:
                print(mfail)

        #checking the total of credits p,d,f equal to 120              
        total = p + d + f
            
        if total != 120:
            print('Total incorrect.\n')

        else:
            break

    if (p == MARKS[0] and d == MARKS[-1] and f == MARKS[-1]):                #assigning the enterd user values to identify the result
        print('Progress')
        

    elif (p == MARKS[1] and (d in MARKS[-2:]) and (f in MARKS[-2:])):
        print('Progress (module trailer)')
        

    elif ((p in MARKS[2:]) and (d in MARKS) and (f in MARKS[3:])):
        print('Do not Progress – module retriever')
        

    elif ((p in MARKS[-3:]) and (d in MARKS[-3:]) and (f in MARKS[:3])):
        print('Exclude')
        
            
    else:
        print('Out of range')