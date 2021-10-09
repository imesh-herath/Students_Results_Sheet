#Getting varriables
result = 0

#Make a List using the marks
MARKS_LIST = [[120,0,0], [100,20,0], [100,0,20], [80,20,20], [60,40,20], [40,40,40], [20,40,60], [20,20,80], [20,0,100], [0,0,120]]

progress, trailer, retriever, excluded = 0, 0, 0, 0

def results():  #defining a function name results
    for i in range (len(MARKS_LIST)):       #checking the number of items in the list

        result = MARKS_LIST[i]

        #process
        if (result == MARKS_LIST[0]):
            print('Progress')
            global progress
            progress += 1

        elif (result == MARKS_LIST[1]):
            print('Progress (module trailer)')
            global trailer
            trailer += 1
        
        elif (result == MARKS_LIST[2]):
            print('Progress (module trailer)')
            trailer += 1

        elif (result == MARKS_LIST[3]):
            print('Do not Progress – module retriever')
            global retriever
            retriever += 1

        elif (result == MARKS_LIST[4]):
            print('Do not Progress – module retriever')
            retriever += 1
        
        elif (result == MARKS_LIST[5]):
            print('Do not Progress – module retriever')
            retriever += 1

        elif (result == MARKS_LIST[6]):
            print('Do not Progress – module retriever')
            retriever += 1

        elif (result == MARKS_LIST[7]):
            print('Exclude')
            global excluded
            excluded += 1
        elif (result == MARKS_LIST[8]):
            print('Exclude')
            excluded += 1
        
        elif (result == MARKS_LIST[9]):
            print('Exclude')
            excluded += 1

results()    #Calling the above function       

#process and printing the Histogram 
print('\n')
print('-'*70) 
print('Horizontal Histogram \n')
print('Progress  ' + str(progress) + ':' + '*' * progress)
print('Trailer   ' + str(trailer) + ':' + '*' * trailer)
print('Retriever ' + str(retriever) + ':' + '*' * retriever)
print('Excluded  ' + str(excluded) + ':' + '*' * excluded)

histogram_total = progress + trailer + retriever + excluded
print('\n')
print(histogram_total,'outcomes in total.')
print('-'*70)