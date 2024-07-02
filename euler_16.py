# Author: Matthew Wygal
# GitHub username: matthew-wy
# Description: Euler Problem 16 - What is the sum of the digits of the number 2^1000?
# Expected output - 1366

# foreseeing using some string typing and splicing here

def power_digit_sum(base, exponent):
    """
    Function to calculate the sum of the digits of a given exponent expression. Takes the calculated number,
    turns it into a string, makes a list from that string, and then makes a new list of integers from the
    stringed list. Then, iterative summing finishes the function out.
    """

    full_number = base ** exponent
    num_string_list = list(str(full_number))

    # now to make a list of actual numbers
    num_int_list = []

    for ch in num_string_list:
        num_int_list.append(int(ch))   # challenge....try this again with list comprehension later

    sums = 0
    for num in num_int_list:
        sums = sums + num

    print(full_number)

    return sums


if __name__ == '__main__':
    print(power_digit_sum(2, 1000))
