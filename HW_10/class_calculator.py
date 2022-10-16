"""
Calculator class with methods
|  Addition                      |
|  Subtraction                   |
|  Multiply                      |
|  Division                      |
|  The remainder of the division |
|  Exponentiation                |
"""


class Calculator:
    """class Calculator"""

    @staticmethod
    def add(first_number, second_number):
        """static addition method"""
        return first_number + second_number

    @staticmethod
    def sub(first_number, second_number):
        """static subtraction method"""
        return first_number - second_number

    @staticmethod
    def mul(first_number, second_number):
        """static multiplication method"""
        return first_number * second_number

    @staticmethod
    def div(first_number, second_number):
        """static division method"""
        return first_number / second_number

    @staticmethod
    def mod(first_number, second_number):
        """static method of finding the remainder of the division"""
        return first_number % second_number

    @staticmethod
    def pow(first_number, second_number):
        """static exponentiation method"""
        return first_number**second_number
