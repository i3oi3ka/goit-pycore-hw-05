"""
task 1
"""


def caching_fibonacci() -> callable:
    """
    Returns a callable function that calculates Fibonacci numbers with caching.

    The returned function uses memoization to store previously computed Fibonacci
    numbers, improving performance by avoiding redundant calculations.

    Returns:
        callable: A function that takes an integer `n` and returns the `n`-th Fibonacci number.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Calculates the `n`-th Fibonacci number using a recursive approach with caching.

        Args:
            n (int): The position in the Fibonacci sequence to calculate.

        Returns:
            int: The `n`-th Fibonacci number.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Create a Fibonacci function with caching
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
print(fib(-1))
