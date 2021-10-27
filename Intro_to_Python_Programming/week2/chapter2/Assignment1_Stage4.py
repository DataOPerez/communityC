##CIS 2531 - Chapter 2
##Assignment 1 - Basic Computations
##Name:
##Date:



#You may delete these comments add your calculations below
#initialize all variable used in the print statements
#Your variables must be assigned through an algebraic statement and not hardcoded values.

#initialize coin values
QUARTER_VALUE = .25
DIME_VALUE = .10
NICKLE_VALUE = .05
PENNY_VALUE  = .01

#initialize dollar values
TWENTY_VALUE = 20
TEN_VALUE = 10
FIVE_VALUE = 5
ONE_VALUE = 1

twenties = 0
tens = 0
fives = 0
ones = 0

#initialize additional values
currentChange = 0

#input coins
quarters = int(input('Enter a number of quarters: '))
dimes = int(input('Enter a number of dimes: '))
nickels = int(input('Enter a number of nickels: '))
pennies = int(input('Enter a number of pennies: '))
CHANGE = (quarters * QUARTER_VALUE) + (dimes * DIME_VALUE) + (nickels * NICKLE_VALUE) + (pennies * PENNY_VALUE)


#twenty calculation
twenties = CHANGE // TWENTY_VALUE
currentChange += TWENTY_VALUE * twenties


#tens calculation
tens = (CHANGE - currentChange) // TEN_VALUE
currentChange += TEN_VALUE * tens


#five calculation
fives = (CHANGE - currentChange) // FIVE_VALUE
currentChange += FIVE_VALUE * fives


#one calculation
ones = (CHANGE - currentChange) // ONE_VALUE
currentChange += ONE_VALUE * ones


#quarter calculation
quarters = (CHANGE - currentChange) // QUARTER_VALUE
currentChange += QUARTER_VALUE * quarters


#dime calculation
dimes = (CHANGE - currentChange) // DIME_VALUE
currentChange += DIME_VALUE * dimes


#nickle calculation
nickels = (CHANGE - currentChange) // NICKLE_VALUE
currentChange += NICKLE_VALUE * nickels


#penny calculation
pennies = (CHANGE - round(currentChange,1)) // PENNY_VALUE
currentChange += PENNY_VALUE * pennies


#output
print(f"Number of coins for ${CHANGE} in change is: \n")

print(f"Twenties: {format(twenties, '.0f')} ")
print(f"Tens: {format(tens, '.0f')}")
print(f"Fives: {format(fives, '.0f')}")
print(f"Ones: {format(ones, '.0f')}")


print(f"Quarters: {format(quarters, '.0f')} ")
print(f"Dimes: {format(dimes, '.0f')}")
print(f"Nickels: {format(nickels, '.0f')}")
print(f"Pennies: {format(pennies, '.0f')}")


