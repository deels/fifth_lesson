# TODO: Task 1
#  The greatest number
#  Write a Python program to get the largest number from a list of random numbers with the length of 10
#  Constraints: use only while loop and random module to generate numbers.

from random import randint
number_list = []
while len(number_list) in range(10):
    number_list.append(randint(10, 100))

print(number_list)
print(max(number_list))
