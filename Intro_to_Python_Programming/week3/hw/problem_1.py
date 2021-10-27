#this explains the program to the user
print("The following program will print all odd intergers from 1 up to a given number.")
print("The program will not include your number.")

#input
maxNumber = int(input("Please enter the given number: "))


#an odd number will always leave a remainder.
#using remainder divison we can check each value in a for loop
#the foor loop takes the number divides it by 2 and checks if the remainder does not equal 0
#if the 0 then the number is considered 
for i in range(1, maxNumber + 1):
    if  i % 2  != 0:
        print(i) #if it doesn't equal 0 then we can assume the integer is odd and print it
        

