#initialize
nextNumber = 0
numberOne = 1
numberTwo = 1

counter = 0

#ask how many Fibonacci numbers the user would like to see
fibNumbers = int(input("Enter how many Fibonacci numbers you want to see: "))

#while loop checks if counter is less than the total Fibonacci numbers.
while counter < fibNumbers:
    print(numberOne, end=" ") #print the first number
    
    nextNumber = numberOne + numberTwo #get the result of the next number by adding 1st number and 2nd number
    numberOne = numberTwo #make the first number the second number
    numberTwo = nextNumber #make the second number the "next number"
    
    counter += 1 #counter increases
