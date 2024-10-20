"""
This file using our functions display demanded data.
Such as the least common multiple of two numbers and
print prime numbers of given range.
"""
from Eratosthenes import eratosthenes
from LeastCommonMultiple import least_common_multiple

if __name__ == '__main__':
    limit = 100
    print("List of prime numbers from 2 to "
          + str(limit) + ": " + str(eratosthenes(limit)))

    value1, value2 = 192, 348
    print("Least common multiple of given values (" + str(value1) + "; "
          + str(value2) + "): " + str(least_common_multiple(value1, value2)))
