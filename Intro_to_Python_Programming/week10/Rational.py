class Rational(object):
    """This creates a rational number (fraction)"""
    def __init__(self, numerator=0, denominator=1):
        """Constructor for a rational number with a numerator and denominator"""
        #remove pass instruction before you begin
        self.__originalNumertator = numerator
        self.__originalDenominator = denominator
        self.__reducedNumerator = numerator
        self.__reducedDenomiator = denominator
        self.reduce()        

    def getOriginal(self):
        """returns a string representation of the original rational number"""
        #remove pass instruction before you begin
        return f"{self.__originalNumertator}/{self.__originalDenominator}"

    def getDecimal(self):
        """returns a string representatin of the rational number in decimal form"""
        #remove pass instruction before you begin
        decimal = self.__originalNumertator / self.__originalDenominator
        return f"{decimal}"

    def reduce(self):
        """reduces the rational number """
        #remove pass instruction before you begin
        gcf = self.__getGCF(self.__originalNumertator, self.__originalDenominator)
        self.__reducedNumerator = (self.__reducedNumerator / gcf)
        self.__reducedDenomiator = (self.__reducedDenomiator / gcf)
        

    def getRational(self):
        """return a string representation of the reduced rational number"""
        #remove pass instruction before you begin
        return f"{format(self.__reducedNumerator, '.0f')}/{format(self.__reducedDenomiator, '.0f')}"

    def displayData(self):
        print()
        print(self.getOriginal() + " equals "+ self.getDecimal() + " and ")
        print(self.getOriginal() +" reduces to " + self.getRational())
        print()

    def __getGCF(self,num1:int, num2:int):
        """returns the greatest common factor of 2 integer values"""
        rem = None
        gcf = None
        while (rem != 0):
            rem = num1 % num2
            if (rem == 0):
                gcf = num2
            else:
                num1 = num2
                num2 = rem
        return gcf;

    @staticmethod
    def multiply(rationalNum1, rationalNum2):
        newNumerator = rationalNum1.__originalNumertator * rationalNum2.__originalNumertator
        newDenominator = rationalNum1.__originalDenominator * rationalNum2.__originalDenominator

        newRationalNum = Rational(newNumerator, newDenominator)
        return newRationalNum


    @staticmethod
    def divide(rationalNum1, rationalNum2):
        newNumerator = rationalNum1.__originalNumertator * rationalNum2.__originalDenominator
        newDenominator =  rationalNum1.__originalDenominator * rationalNum2.__originalNumertator

        newRationalNum = Rational(newNumerator, newDenominator)
        return newRationalNum


    @staticmethod
    def add(rationalNum1, rationalNum2):

        num = (rationalNum1.__reducedNumerator * rationalNum2.__reducedDenomiator) + (rationalNum2.__reducedNumerator * rationalNum1.__reducedDenomiator)
        den = (rationalNum1.__reducedDenomiator * rationalNum2.__reducedDenomiator)
        newRationalNum = Rational(num, den)
        return newRationalNum

    @staticmethod
    def subtract(rationalNum1, rationalNum2):
        num = (rationalNum1.__reducedNumerator * rationalNum2.__reducedDenomiator) - (rationalNum2.__reducedNumerator * rationalNum1.__reducedDenomiator)
        den = (rationalNum1.__reducedDenomiator * rationalNum2.__reducedDenomiator)
        newRationalNum = Rational(num, den)

        return newRationalNum



