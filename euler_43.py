# Author: Matthew W
# GitHub username: matthew-wy
# Description: Euler Problem 43
# observe the 0-9 pandigital number 1406357289
# let d1 be the 1st digit, d2 the second digit ... dsubn the nth digit
# this number has the property:
# d2d3d4 = 406 = divisible by 2
# d3d4d5 = 063 = divisible by 3
# d4d5d6 = 635 = divisible by 5
# d5d6d7 = 357 = divisible by 7
# d6d7d8 = 572 = divisible by 11
# d7d8d9 = 728 = divisible by 13
# d8d9d10 = 289 = divisible by 17
# find the sum of all 0-9 pandigital numbers with this property
# Expected output - tba

def pandigital_subdiv_sum():
    """
    Function to find the sum of all 0-9 pandigital numbers with the property that
    d2d3d4 is divisible by 2, d3d4d5 is divisible by 3......d8d9d10 is divisible by 17
    (each 3 digit subset starting with d2 is divisible by the next prime)
    """

    pandig_sum = 0

    for num in range(1234567890, 9087654321+1):  # set our lower and upper bounds
        # make the num a list and check if the digits are unique
        num_str = str(num)
        num_list = [int(x) for x in num_str]

        # make sure the number has unique digits (ten, 0-9)
        if unique_digit(num_list, 10):

            # then check if the subdivisibility property is there
            # and if it is, add the number to the sum
            if subdiv_check(num):
                pandig_sum = pandig_sum + num

    return pandig_sum


def unique_digit(num_list, n):
    """
    Function to check if a passed list of n digits has all unique digits or not.
    Utilizes sets to check and returns True or False.
    """
    num_set = set(num_list)
    return len(num_set) == n


def subdiv_check(num):
    """
    Function to check if a passed number possesses the subdivisibility property as described in the
    program header. For this program, num is assumed to be 0-9 pandigital.
    """
    subdiv_flag = True  # flag to return at the end after all checks
    test_sum = 0

    num_str = str(num)
    num_list = [int(x) for x in num_str]

    # d2d3d4 divisible by 2
    test_sum = num_list[1] + num_list[2] + num_list[3]
    if test_sum % 2 != 0:
        subdiv_flag = False

    # d3d4d5 divisible by 3
    test_sum = num_list[2] + num_list[3] + num_list[4]
    if test_sum % 3 != 0:
        subdiv_flag = False

    # d4d5d6 divisible by 5
    test_sum = num_list[3] + num_list[4] + num_list[5]
    if test_sum % 5 != 0:
        subdiv_flag = False

    # d5d6d7 divisible by 7
    test_sum = num_list[4] + num_list[5] + num_list[6]
    if test_sum % 7 != 0:
        subdiv_flag = False

    # d6d7d8 divisible by 11
    test_sum = num_list[5] + num_list[6] + num_list[7]
    if test_sum % 11 != 0:
        subdiv_flag = False

    # d7d8d9 divisible by 13
    test_sum = num_list[6] + num_list[7] + num_list[8]
    if test_sum % 13 != 0:
        subdiv_flag = False

    # d8d9d10 divisible by 17
    test_sum = num_list[7] + num_list[8] + num_list[9]
    if test_sum % 17 != 0:
        subdiv_flag = False

    return subdiv_flag


# tests
print(pandigital_subdiv_sum())
