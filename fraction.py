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

    def __init__(self, numerator1, denominator1, numerator2, denominator2):
        """
        Initialize the FractionCalculator with two fractions.

        Parameters
        ----------
        numerator1 : int
            Numerator of the first fraction.
        denominator1 : int
            Denominator of the first fraction.
        numerator2 : int
            Numerator of the second fraction.
        denominator2 : int
            Denominator of the second fraction.
        """
        self.fraction1 = Fraction(numerator1, denominator1)
        self.fraction2 = Fraction(numerator2, denominator2)

    def main(self):
        """Handle welcome statement, user input, and function routing logic."""
        func_type = input("Welcome to the Fraction Calculator.  What type"
                          " of calcuation do you need to perform?  \nPlease"
                          "choose from the following: add, subtract, "
                          "multiply, or divide:  ")
        numerator1 = input("\nEnter the integer value for numerator 1:  ")
        numerator2 = input("Enter the integer value for numerator 2:  ")
        denominator1 = input("Enter the integer value for denominator 1:  ")
        denominator2 = input("Enter the integer value for denominator 2:  ")

        try:
            func_type = func_type.lower()
            if func_type in ['add', 'subtract', 'multiply', 'divide']:
                match func_type:
                    case 'add':
