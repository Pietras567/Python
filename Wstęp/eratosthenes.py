"""This file calculates prime numbers from 2 to n."""
import math


def eratosthenes(limit):
    """Return the list of prime numbers from 2 to n."""
    if limit <= 1:
        raise ValueError("limit must be greater than 1")

    is_prime = [True] * (limit+1)

    for i in range(2, int(math.sqrt(limit))+1):

        if is_prime[i] is True:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    output = []

    for i in range(len(is_prime)):
        if is_prime[i] is True and i >= 2:
            output.append(i)

    return output
