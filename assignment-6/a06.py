## IMPORTS GO HERE

## END OF IMPORTS
def cumulative_marks(inputList):
    if inputList == None:
        return None
    if inputList == []:
        return inputList   
    myFinalList = []
    for i in range (0,len(inputList)):
        sumTotal = 0
        myList = []
        roll_no = inputList[i][0][1:3]+"P"+"-"+inputList[i][0][3:]
        if len(inputList[i]) == 2:
            pass
        else: 
            for j in range (2,len(inputList[i])):
                if type(inputList[i][j]) == int or type(inputList[i][j]) == float:
                    sumTotal += (inputList[i][j])
                else:
                    continue
        myList.append(roll_no)
        myList.append(inputList[i][1])
        myList.append(sumTotal)
        myTuple = tuple(myList)
        myFinalList.append(myTuple)
    return(myFinalList)

### YOUR CODE FOR cumulative_marks() FUNCTION GOES HERE ###

#### End OF MARKER

if __name__ == '__main__':
    results = [
        ('p101111', 'Muhammad Amin', 64, 78.5, 89, 25, 99),
        ('p101112', 'Tehseen Khan', 14, 28.5, 83, 76),
        ('p101113', 'Tauqeer Ali', 87, None, 1.6)
    ]

#    print cumulative_marks(results)
    # output: [('10P-1111', 'Muhammad Amin', 355.5), ('10P-1112', 'Tehseen Khan', 201.5), ('10P-1113', 'Tauqeer Ali', 88.6)]

