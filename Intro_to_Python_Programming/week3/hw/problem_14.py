NUMBER = 19
totalCheck = 0 
isFactor = False

#loop goes through all our numbers starting from 1 through NUMBER
for i in range(1, NUMBER):
    isFactor = False
    if NUMBER % i == 0: #checks for a remainder
        totalCheck += i #if no remainder add the number to the running total.

#check if totalCheck equals NUMBER if True tell user otherwise tell user no.
if totalCheck == NUMBER:
    print(f"{NUMBER} is a perfect number!")

else:
    print(f"{NUMBER} is not a perfect number.")
