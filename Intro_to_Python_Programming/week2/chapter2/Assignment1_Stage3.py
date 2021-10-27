##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name:
##Date:



#You may delete these comments add your calculations below
#initialize all variable used in the print statements
#Your variables must be assigned through an algebraic statement and not hardcoded values.

#initialize values
QUARTER_VALUE = .25
DIME_VALUE = .10
NICKLE_VALUE = .05
PENNY_VALUE  = .01

quarters = int(input('Enter a number of quarters: '))
dimes = int(input('Enter a number of dimes: '))
nickels = int(input('Enter a number of nickels: '))
pennies = int(input('Enter a number of pennies: '))
CHANGE = (quarters * QUARTER_VALUE) + (dimes * DIME_VALUE) + (nickels * NICKLE_VALUE) + (pennies * PENNY_VALUE)
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


print(f"Number of coins for ${CHANGE} in change is: \n")
print(f"Quarters: {format(quarters, '.0f')} ")
print(f"Dimes: {format(dimes, '.0f')}")
print(f"Nickels: {format(nickels, '.0f')}")
print(f"Pennies: {format(pennies, '.0f')}")
