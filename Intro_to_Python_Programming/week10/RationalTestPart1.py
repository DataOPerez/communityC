from Rational import *

def enterData():
    '''Allows user to enter a valid numerator and denominator'''
    num = ""
    den = ""
    while num == "" or den == "" or den == "0":
        num = input("Please enter the numerator   ---> ")
        den = input("Please enter the denominator ---> ")
    num = int(num)
    den = int(den)
    return num, den

def main():
    '''main method, creates a Rational number and displays information about it'''
    num, den = enterData()
    rationalNumber = Rational(num, den)
    rationalNumber.displayData()


main()
input("press enter to quit")
