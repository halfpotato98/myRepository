import re
import string

def PrintList(): 
    from collections import Counter #import counter function
    from collections import OrderedDict
    import operator
    with open("InputFile.txt") as file_in: #open file
        myList = [] #initialize myList
        for line in file_in: #for each line in file
            myList.append(line) #add an entry to the list
    strippedList = list(map(str.strip, myList)) #get rid of new line characters
    counter = Counter(strippedList) #create a dictionary of frequencies using stripped list
    sorted1 = sorted(counter.items(),key=operator.itemgetter(1),reverse=True) #sort in descending order
    for key, value in sorted1: 
        print ('{}: {}'.format(key, value)) #output
    return 0


def PrintParticular(myInput):
    from collections import Counter #import counter function
    with open("InputFile.txt") as file_in: #open file
        myList = [] #initialize myList
        for line in file_in: #for each line in file
            myList.append(line) #add an entry to the list
    strippedList = list(map(str.strip, myList)) #get rid of new line characters
    counter = Counter(strippedList) #create a dictionary of frequencies using stripped list
    myNum = counter[myInput.capitalize()]
    return myNum #return the number of products for c++ to output

def PrintHistogram():
    from collections import Counter #import counter function
    from collections import OrderedDict
    import operator
    with open("InputFile.txt") as file_in: #open file
        myList = [] #initialize myList
        for line in file_in: #for each line in file
            myList.append(line) #add an entry to the list
    strippedList = list(map(str.strip, myList)) #get rid of new line characters
    counter = Counter(strippedList) #create a dictionary of frequencies using stripped list
    strDict = repr(counter)
    f = open("outputFrequencies.txt", "w+")
    sorted1 = sorted(counter.items(),key=operator.itemgetter(1),reverse=True) #sort in descending order
    for key, value in sorted1: #sorted1 does not need .items() because .items is in previous line
        strLine = repr('{}: {}'.format(key, value)) #output
        newString = strLine[1:-1]
        f.write(newString + "\n") #write to file
    f.close()

    f2 = open("outputFrequencies.txt", "r") #open for read only
    for line in f2:
        x = line.split(": ") #split at :
        print (x[0], end = '') #print product
        for y in range(int(x[1])):  #print '=' for each product
            print("=", end = '') #no new line
        print("") #new line
    f2.close #close file
    return 0



