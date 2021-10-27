##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name:
##Date:

CHANGE = 97
#You may delete these comments add your calculations below
#initialize all variable used in the print statements
#Your variables must be assigned through an algebraic statement and not hardcoded values.

#initialize values
QUARTER_VALUE = 25
DIME_VALUE = 10
NICKLE_VALUE = 5
PENNY_VALUE  = 1

quarters = 0
dimes = 0
nickels = 0
pennies = 0
currentChange = 0 

#quarter calculation
quarters = CHANGE // QUARTER_VALUE
currentChange += QUARTER_VALUE * quarters
#print('current change: ', currentChange)

#dime calculation
dimes = (CHANGE - currentChange) // DIME_VALUE
currentChange += DIME_VALUE * dimes
#print('current change: ', currentChange)

#nickle calculation
nickels = (CHANGE - currentChange) // NICKLE_VALUE
currentChange += NICKLE_VALUE * nickels
#print('current change: ', currentChange)

#penny calculation
pennies = (CHANGE - currentChange) // PENNY_VALUE
currentChange += PENNY_VALUE * pennies
#print('current change: ', currentChange)


print(f"Number of coins for {CHANGE} cents in change is: \n")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")
