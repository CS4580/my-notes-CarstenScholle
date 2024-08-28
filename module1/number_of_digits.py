"""Library to calculate the number of digits for different algorithms
"""
from math import factorial


def factorial_length(number):
    """Count the number of digits in a factorial number

    Args:
        number (int): integer value to calculate factorial

    Returns:
        int: number of digits for factorial of input
    """
    length = 0
    factorial_number = factorial(number)
    length = len(str(factorial_number))
    return length


def main():
    """Driven Function
    """
    number = 120
    digits = factorial_length(number)
    print(f"You have {digits} digits in factorial {number}")


if __name__ == '__main__':
    main()