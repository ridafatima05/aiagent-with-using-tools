from agents import function_tool

# A good tool is one with clear and precise documentation.
@function_tool
def addition(n1: int, n2: int):
    """
    Performs the addition of two integers.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A formatted string containing the sum of the two numbers.
    """
    print("Addition tool fire...")
    return f"Your answer is {n1 + n2}."


@function_tool
def subtract(n1: int, n2: int):
    """
    Performs the subtraction of two integers.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A formatted string containing the difference of the two numbers.
    """
    print("Substraction tool fire...")
    return f"Your answer is {n1 - n2}."


@function_tool
def multiply(n1: int, n2: int):
    """
    Performs the multiplication of two integers.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.

    Returns:
        str: A formatted string containing the product of the two numbers.
    """
    print("Multiplication tool fire...")
    return f"Your answer is {n1 * n2}."


@function_tool
def division(n1: int, n2: int):
    """
    Performs the division of two integers.

    Args:
        n1 (int): The numerator.
        n2 (int): The denominator.

    Returns:
        str: A formatted string containing the result of the division,
        or an error message if division by zero is attempted.
    """
    print("Division tool fire...")
    try:
        result = n1 / n2
        return f"Your answer is {result}."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
