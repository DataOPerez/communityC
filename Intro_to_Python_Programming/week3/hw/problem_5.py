maxNumbers = 0
userInput = 0

#explain the program to the user
print("""The following program will take a specific number of integers and
determine the smallest integer \n""")

#input the total number of integers and the user's first value, assuming it's the smallest
maxNumbers = int(input("How many number of integers would you like to test: "))
firstNumber = int(input("Enter your first number: "))
                
#this for loop will continue asking the user for more intergers
for i in range(maxNumbers-1): #i used - 1 since the user enters their first value above.
    otherNumber = int(input("Enter the next number: "))
    if otherNumber < firstNumber: #this checks which number is bigger if other number is bigger than first entry replace it.
        firstNumber = otherNumber

#letting the user know their smallest number.
print(f"Your smallest integer is {firstNumber}.")
