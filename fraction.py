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
        print("Welcome to the Fraction Calculator.")
        while True:
            func_type = input(
                "What calculation do you need to perform? Choose: "
                "add, subtract, multiply, or divide: "
            ).strip().lower()

            try:
                fraction1 = Fraction(input('Enter first fraction (a/b): '))
                fraction2 = Fraction(input('Enter second fraction (a/b): '))

                if func_type in ['add', 'subtract', 'multiply', 'divide']:
                    match func_type:
                        case 'add':
                            self.add(fraction1, fraction2)
                        case 'subtract':
                            self.subtract(fraction1, fraction2)
                        case 'multiply':
                            self.multiply(fraction1, fraction2)
                        case 'divide':
                            self.divide(fraction1, fraction2)
                    break  # Exit after a successful calculation
                else:
                    print("Invalid calculation type entered.")
            except ZeroDivisionError:
                print("Error: Division by zero is undefined, please try "
                      "again.")
            except ValueError:
                print("Invalid input. Enter fractions in 'a/b' format.")

    def add(self, fraction1, fraction2):
        """Return the sum of fraction1 and fraction2."""
        result = fraction1 + fraction2
        print(f'\nThe result of adding {fraction1} and {fraction2} '
              f'equals {result}')

    def subtract(self, fraction1, fraction2):
        """Return the difference of fraction1 and fraction2."""
        result = fraction1 - fraction2
        print(f'\nThe result of subtracting {fraction2} from {fraction1} '
              f'equals {result}')

    def multiply(self, fraction1, fraction2):
        """Return the product of fraction1 and fraction2."""
        result = fraction1 * fraction2
        print(f'\nThe result of multiplying {fraction1} and {fraction2} '
              f'equals {result}')

    def divide(self, fraction1, fraction2):
        """Return the division of fraction1 by fraction2."""
        try:
            result = fraction1 / fraction2
            print(f'\nThe result of dividing {fraction1} by {fraction2} '
                  f'equals {result}')
        except ZeroDivisionError:
            print("Error: Division by zero is undefined.")


if __name__ == "__main__":
    frac_calculator = FractionCalculator()
    frac_calculator.main()
