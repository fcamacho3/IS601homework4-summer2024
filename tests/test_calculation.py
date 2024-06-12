# pylint: disable=unnecessary-dunder-call, invalid-name, line-too-long, trailing-whitespace, missing-final-newline

""" This module will test at the individual Calculation level """
from decimal import Decimal
from typing import Callable
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

#Turns each 'row' which is a tuple of elements into parameters
#testing different numbers/type combos to ensure correctedness
# @pytest.mark.parametrize("a, b, operation, expected", [
#     (Decimal('10'), Decimal('5'), add, Decimal('15')),
#     (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
#     (Decimal('10'), Decimal('5'), multiply, Decimal('50')),
#     (Decimal('10'), Decimal('2'), divide, Decimal('5')),
#     (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
#     (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
#     (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
#     (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
# ])

def test_calc_perform(a: Decimal,b: Decimal, operation: Callable[[Decimal, Decimal], Decimal],
                      expected: Decimal):
    '''tests for the single calculation instance'''
    calc = Calculation(a, b, operation)
    #perform and ensure its as expected
    # comma , onwards = fail message
        # if failed, print out exactly what inputs were used and how it failed with which operation
        # operation.name prints out function name that was called
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calc_repr():
    '''tests the string representation output'''
    calc = Calculation(Decimal('5'), Decimal('10'), add)
    expected = "Calculation(5, 10, add)"
    #ensure fail message has been added
    assert calc.__repr__() == expected, '''The '__repr__' method failed to output the
     expected response.'''

def test_div_by_zero():
    '''testing the divide by zero functionality'''
    calc = Calculation(Decimal('5'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()


# """
# This module contains tests for the calculator operations and Calculation class.

# The tests are designed to verify the correctness of basic arithmetic operations
# (addition, subtraction, multiplication, division) implemented in the calculator.operations module,
# as well as the functionality of the Calculation class that encapsulates these operations.
# """

# # Import statements:
# # Disable specific pylint warnings that are not relevant for this test file.
# # Import the Decimal class for precise decimal arithmetic, which is especially useful in financial calculations.
# # Import pytest for writing test cases.
# # Import the Calculation class from the calculator package to test its functionality.
# # Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# # pylint: disable=unnecessary-dunder-call, invalid-name
# from decimal import Decimal
# import pytest
# from calculator.calculation import Calculation
# from calculator.operations import add, subtract, multiply, divide

# # pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# # with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# # with both integer and decimal operands to ensure the operations work correctly under different conditions.

# def test_calculation_operations(a, b, operation, expected):
#     """
#     Test calculation operations with various scenarios.
    
#     This test ensures that the Calculation class correctly performs the arithmetic operation
#     (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
#     and that the result matches the expected outcome.
    
#     Parameters:
#         a (Decimal): The first operand in the calculation.
#         b (Decimal): The second operand in the calculation.
#         operation (function): The arithmetic operation to perform.
#         expected (Decimal): The expected result of the operation.
#     """
#     calc = Calculation(a, b, operation)  # Create a Calculation instance with the provided operands and operation.
#     assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

# def test_calculation_repr():
#     """
#     Test the string representation (__repr__) of the Calculation class.
    
#     This test verifies that the __repr__ method of a Calculation instance returns a string
#     that accurately represents the state of the Calculation object, including its operands and operation.
#     """
#     calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
#     expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
#     assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

# def test_divide_by_zero():
#     """
#     Test division by zero to ensure it raises a ValueError.
    
#     This test checks that attempting to perform a division operation with a zero divisor
#     correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
#     """
#     calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
#     with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
#         calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.