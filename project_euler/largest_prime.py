"""
Given a number, what is its largest prime factor.
"""


def largest_prime(number):
    largest_prime_factor = 2
    print largest_prime_factor
    for i in range(number):
        print i
        if (i % 2 != 0 and i % 3 != 0) and number % i == 0:
            largest_prime_factor = i
    return largest_prime_factor


def print_prime(n):
    for i in range(n):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            print i
    return i
