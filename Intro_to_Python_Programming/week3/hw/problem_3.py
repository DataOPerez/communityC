total = 0
maxNumber = 0

print("The following program will sum all integers from 1 up to a given number.")
maxNumber = int(input("Enter the final number, (your number will be included in the sum: "))

for i in range(maxNumber + 1):
    total += i

print(f"Your total is: {total}")
