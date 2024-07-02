# Author: Matthew Wygal
# GitHub username: matthew-wy
# Description: Euler Problem 1 - Find the sum of all the multiples of 3 or 5 below 1000.
# Sounding like a good discrete math problem, isn't it?

# Following the problems encounter in counting section of discrete mathematics:
# 1000//3 + 1000//5 - 1000//lcm(3,5) = number of multiples of 3 or 5 below 1000
# However, this does not tell us what those multiples are...

# let's try an iterative approach with a for loop

multiple_3_5_list = []  # initialize empty list to store our multiples
sum_multiples = 0  # initialize empty int for our final sum

for i in range(1, 1000):  # we are placing 1000 as max of range since the problem calls for 'below' 1000
    if i % 3 == 0 or i % 5 == 0:
        multiple_3_5_list.append(i)

for num in multiple_3_5_list:
    sum_multiples = sum_multiples + num

print(sum_multiples)
