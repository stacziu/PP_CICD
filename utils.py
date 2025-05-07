"""
Exemplary calculator functions
"""


def add(a: int, b: int) -> int:
    """Sum of two numbers"""

    return a + b


def subtract(a: int, b: int) -> int:
    """Difference of two numbers"""

    return a - b


def multiply(a: int, b: int) -> int:
    """Multiplication of two numbers"""

    return a * b


def divide(a: int, b: int) -> float:
    """Division of two numbers"""

    return a / b


def binary_conversion(a) -> str:
    """Converting integer to binary"""
    if a < 0 or a > 100:
        raise ValueError("Not in range")
    if not isinstance(a, int):
        raise ValueError("Not an integer")

    if a == 0:
        return "0"
    res = ""
    while a > 0:
        res = str(a % 2) + res
        a //= 2
    return res
