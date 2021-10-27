keepGoing = ""
totalOfScores = 0
counter = 0

#explain program
print("This program will calculate the average of a set of test scores.")
while keepGoing != "-1":
    userInput = float(input("Enter a score: ")) #get input
    totalOfScores += userInput #add scores together
    counter += 1 #increase counter to divided by at the end

    keepGoing = input("\nIf you'd like to stop, type: -1\nTo continue press enter:\n")

print(f"{round((totalOfScores/counter),2)}") #divide the totalOfScores by the counter to get average.
    
