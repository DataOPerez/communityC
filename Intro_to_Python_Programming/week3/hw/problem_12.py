#input number as a string
number = input("Enter a number to see the sum of all the digits in that number: ")
total = 0

for char in number: #loop through the number character by chacter
    convertNumber = int(char) #for each character convert it to a int
    total += convertNumber #add it to total

print(f"sum of digits: {total}") #print total at the end
