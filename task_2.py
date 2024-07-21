"""
task 2
"""

import re
from typing import Callable

def generator_numbers(text: str):
    """
    A generator function that extracts numbers from a given text string.

    This function uses a regular expression pattern to find all numbers in the text,
    including integers and floating-point numbers. It yields each number as a float.

    Args:
        text (str): The input text from which to extract numbers.

    Yields:
        float: The next number found in the text as a float.
    """
    pattern = re.compile(r"\b\d+\.?\d*\b")
    index = 0
    while match := pattern.search(text, index):
        yield float(match.group())
        index = match.end()

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    """
    Sums all numbers extracted from the input text using the provided generator function.

    Args:
        text (str): The input text from which to extract and sum numbers.
        func (Callable[[str], float]): A generator function that extracts numbers from text.

    Returns:
        float: The sum of all extracted numbers.
    """
    return sum(func(text))


string = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, \
доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(string, generator_numbers)
print(f"Загальний дохід: {total_income}")
