def displayScores(scoreArray):
    """Displays the current test scores"""
    print("The current test scores are:")
    for i in range(len(scoreArray)-1):
        print(float(scoreArray[i]), end= "%, ")
    print(float(scoreArray[len(scoreArray)-1]), end = "%\n")
    


def findMin(scoreArray):
    """Finds the minimum value in list passed by parameter"""
    minScore = scoreArray[0]
    for score in scoreArray:
        if score < minScore:
            minScore = score
    return minScore


def findMax(scoreArray):
    """Finds the highest value in the list passed by parameter"""
    maxScore = scoreArray[0]
    for score in scoreArray:
        if score > maxScore:
            maxScore = score
    return maxScore

def dropLowest(scoreArray):
    """Finds the lowest score using findMin() then uses remove() to remove from the parameter. """
    lowestScore = findMin(scoreArray)
    scoreArray.remove(lowestScore)

def getMean(scoreArray):
    total = 0
    for score in scoreArray:
        total += score

    mean = total / len(scoreArray)

    return mean

def getMedian(scoreArray):
    """Sorts the array if array length is even it will get the average of the two numbers.
    num1 is found by dividing the length of the array / 2 then subtracting 1 since the array starts from 0
    num2 is the same but no -1
    
    If the array lenght is odd we simply localte the middle number diving by 2 and subtracing 1"""
    arrayLength = len(scoreArray)
    scoreArray.sort()

    if arrayLength % 2 == 0:
        num1 = scoreArray[int(len(scoreArray) / 2 - 1)]
        num2 = scoreArray[int(len(scoreArray) / 2 )]
        
        median = (num1 + num2) / 2
    else:
        median = (scoreArray[int(round(len(scoreArray)/2) -1 )])
    return median



def main():
    testScores = [90,85,52,74,95,100,78]
    displayScores(testScores)
    print()
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)
    mean = getMean(testScores)
    print("Average: ", mean)
    median = getMedian(testScores)
    print("Median: ", median)
    print()

    dropLowest(testScores)
    print("After dropping the lowest score.")
    testScores.reverse()
    displayScores(testScores)
    mean = getMean(testScores)
    print("Average: ", mean) 
    #ask professor if it's better to two variables or one:
    #we define the mean on like 69 but then I reassign it here.
    median = getMedian(testScores)
    print("Median: ", median)
    
    

if __name__ == '__main__':
    main()
