#quick google search says i can import random and get random integers
from random import randint

#initialize some values
number1 = randint(0, 9)
number2 = randint(0, 9)

correctCounter = 0


#these two lines explain the program
print("The following program will display simple mulitplication problems.")
print("Answer correctly 3 times to finish.")

#this while loop checks if the user has 3 total correct answers
while correctCounter != 3:
    correctAnswer = number1 * number2 #multiples the numbers to get the correct answer.
    usersAnswer = int(input(f"{number1} * {number2} =")) #this displays the question to the user

    #this if statement will check if user was correct
    #if true then tell the user & increase the correctCounter by 1
    #if false then tell the user
    if correctAnswer == usersAnswer:
        correctCounter +=1
        print(f"Correct - {correctCounter}/3 \n")
    else:
        print(f"Incorrect try again - {correctCounter}/3 \n")

#create two new random numbers
    number1 = randint(0, 9)
    number2 = randint(0, 9)

#this tells the users they're done.
print("Great you got 3/3!")
