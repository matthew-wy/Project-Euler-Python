# Author: Matthew Wygal
# GitHub username: matthew-wy
# Description: Euler Problem 2 - find the sum of the even-valued terms of the Fibonacci sequence under 4 million
# Target output - 4613732

# we will approach this as a function - although we may need to change it up in order for submission to count!

def even_fib_sum(maximum):
    """Simple function to calculate the sum of only the even Fibonacci numbers under the given max"""

    even_fib_list = []  # initialize empty list to store the even Fib numbers
    fib_1 = 0  # set variables to reset and calculate further Fib numbers
    fib_2 = 1
    current_fib = 0
    final_sum = 0  # final value to return

    # iterative approach - we can try a recursive approach when we are feeling a bit more masochistic
    while current_fib < maximum:

        current_fib = fib_1 + fib_2

        if current_fib < maximum:
            # we need extra if statement here to not over-calculate
            if current_fib % 2 == 0:  # if our current fib is even
                even_fib_list.append(current_fib)  # then we will append it to our list

        # reset our fib variables for the next pass
        fib_1 = fib_2
        fib_2 = current_fib

    # after we have added all the even Fibonacci numbers, we will then calculate the sum with a for statement
    for num in even_fib_list:
        final_sum = final_sum + num

    return final_sum


if __name__ == '__main__':
    print(even_fib_sum(4000000))
