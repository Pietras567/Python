"""This file calculates the least common multiple of given two values."""
import math


def factorization(value):
    """Return the prime factors of given value."""
    factors = []
    k = 2
    sqrt = math.sqrt(value)

    while value > 1 & k <= sqrt:
        while value % k == 0:
            factors.append(k)
            value = value / k
        k = k + 1

    return factors


def least_common_multiple(value1, value2):
    """Return the value of least common multiple of given two values."""
    least_common_multiple = 1

    if value1 and value2:
        factors1 = factorization(abs(value1))
        factors2 = factorization(abs(value2))
        merge = factors1

        for factor in factors1:
            if factor in factors2:
                factors2.remove(factor)
        merge += factors2

        for i in merge:
            least_common_multiple = least_common_multiple * i

        return least_common_multiple
    raise ValueError("Given values must be integers "
                     "whith a value different from zero.")
