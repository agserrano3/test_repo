def fib(n):
    # If 'n' is 0, raise an error because there is no 0th number in the Fibonacci sequence.
    if n == 0: 
        raise ValueError("Invalid input. There's no zeroth Fibonacci number.")

    # Initialize two variables for the first two Fibonacci numbers.
    a, b = 0, 1

    # Calculate the nth Fibonacci number.
    for _ in range(n - 1):
        a, b = b, a + b

    # Return the nth Fibonacci number.
    return a