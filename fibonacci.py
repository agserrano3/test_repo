def fib(n):
    """
    Return the Fibonacci sequence up to n
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
