# Author: Matthew W
# GitHub username: matthew-wy
# Description: Euler Problem 41 - An n-digit number is pandigital if it makes use of all the digits
# 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
# Expected output - 7652413

def pan_primes():
    """Simple function to calculate the largest n-digit pandigital prime"""

    largest_pan_prime = 0  # initialize

    for num in range(7123455, 7654323, 2):
        # we establish our lower and upper bound because we know that
        # 2,3,5,6,8,9 digit pandigital numbers cannot be prime by rule of divisibility by 3
        # eg: 1+2+3 = 6, divisible by 3
        # thus, we are only concerned with 4 and 7-digit pandigital numbers
        # since we are concerned with the largest, we can omit 4 digit pandigital numbers
        # by assuming that the largest pandigital prime should start with a 7, we achieve the lowest bound
        # of 7123455 and then only check the odd numbers up to the highest pandigital possibility 7654321

        # creating list of numbers for checks
        string_num = str(num)
        num_list = [int(x) for x in string_num]
        digit_sum = sum(num_list)

        # we know that for a given 7 digit pandigital number, the sum of the digits must equal 28
        # so we check for this as well as make sure each digit is unique, and then check for primality
        if digit_sum == 28 and check_unique_dig(num_list, 7) and prime_check(num):
            largest_pan_prime = num

    return largest_pan_prime


def check_unique_dig(num_list, n):
    """
    Function to check if digits are unique within a passed list. Creates a set from the passed list.
    Returns False if 0 is present, and then returns the truth value of if the number of unique elements
    in the set is equal to the expected n that is passed. n is expected number of unique digits.
    """

    num_set = set(num_list)
    if 0 in num_set:
        return False
    # length of a set is how many unique elements there are in the set
    return len(num_set) == n


def prime_check(num):
    """Simple function to return True or False if an int is prime or not"""

    # base cases
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # main check
    for i in range(3, int(num**0.5)+1, 2):  # the final 2 means we are only considering odd numbers
        if num % i == 0:
            return False
    # if we have made it out of all the base cases, we can simply return True
    return True


# test
print(pan_primes())
