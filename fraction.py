"""
Fraction.

Spyder Editor.

Created on Thu Oct 31 01:51:11 2024
@author: BRICE NELSON
"""
from fractions import Fraction


class FractionCalculator:
    """
    A calculator class for performing arithmetic operations on fractions.

    This class allows users to create a fraction calculator object with two
    fractions and perform basic operations, including addition, subtraction,
    multiplication, and division. Fractions are represented using Python's
    standard library Fraction class to ensure precision.

    Attributes
    ----------
    fraction1 : Fraction
        The first fraction for operations.
    fraction2 : Fraction
        The second fraction for operations.

    Methods
    -------
    add():
        Returns the sum of fraction1 and fraction2.
    subtract():
        Returns the difference of fraction1 and fraction2.
    multiply():
        Returns the product of fraction1 and fraction2.
    divide():
        Returns the division of fraction1 by fraction2.
    """

    # def __init__(self, numerator1, denominator1, numerator2, denominator2):
    #     """
    #     Initialize the FractionCalculator with two fractions.

    #     Parameters
    #     ----------
    #     numerator1 : int
    #         Numerator of the first fraction.
    #     denominator1 : int
    #         Denominator of the first fraction.
    #     numerator2 : int
    #         Numerator of the second fraction.
    #     denominator2 : int
    #         Denominator of the second fraction.
    #     """
    #     numerator1 = self.numerator1

    #     self.fraction1 = Fraction(numerator1, denominator1)
    #     self.fraction2 = Fraction(numerator2, denominator2)

    def main(self):
        """Handle welcome statement, user input, and function routing logic."""
        try:
            func_type = input("Welcome to the Fraction Calculator.  What type"
                              " of calcuation do you need to perform?  "
                              "\nPlease choose from the following: add, "
                              "subtract, multiply, or "
                              "divide:  ").strip().lower()
            numerator1 = int(input("\nEnter the integer value for "
                                   "numerator 1:  "))
            numerator2 = int(input("Enter the integer value for "
                                   "numerator 2:  "))
            denominator1 = int(input("Enter the integer value for "
                                     "denominator 1: "))
            denominator2 = int(input("Enter the integer value for "
                                     "denominator 2: "))

            self.fraction1 = Fraction(numerator1, denominator1)
            self.fraction2 = Fraction(numerator2, denominator2)

            func_type = func_type.lower()
            if func_type in ['add', 'subtract', 'multiply', 'divide']:
                match func_type:
                    case 'add':
                        print(f"The result of adding {self.fraction1} and "
                              "{self.fraction2} is: {self.add()}")
                    case 'subtract':
                        print(f"The result of subtracting {self.fraction1} and"
                              " {self.fraction2} is: {self.subtract()}")
                    case 'multiply':
                        print(f"The result of multiplying {self.fraction1} and"
                              " {self.fraction2} is: {self.multiply()}")
                    case 'divide':
                        if self.divide() is not None:
                            print(f"The result of dividing {self.fraction1} by"
                                  " {self.fraction2} is: {self.divide()}")
            else:
                print("Invalid calculation type entered.")
                self.main()

        except ValueError:
            print("Invalid input. Please enter integer values for numerators "
                  "and denominators.")
            self.main()

    def add(self):
        """Return the sum of fraction1 and fraction2."""
        return self.fraction1 + self.fraction2

    def subtract(self):
        """Return the difference of fraction1 and fraction2."""
        return self.fraction1 - self.fraction2

    def multiply(self):
        """Return the product of fraction1 and fraction2."""
        return self.fraction1 * self.fraction2

    def divide(self):
        """Return the division of fraction1 by fraction2."""
        if self.fraction2 == 0:
            print("Cannot divide by zero.")
            return None
        return self.fraction1 / self.fraction2


if __name__ == "__main__":
    frac_calculator = FractionCalculator()
    frac_calculator.main()
