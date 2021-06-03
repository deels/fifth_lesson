# TODO: Task 2
#  Exclusive common numbers.
#  Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the
#  common integers between the 2 initial lists without any duplicates.
#  Constraints: use only while loop and random module to generate numbers.

from random import randint
first_list = []
second_list = []
while len(first_list) in range(10):
    first_list.append(randint(1, 10))
while len(second_list) in range(10):
    second_list.append(randint(1, 10))

first_set = set(first_list)
second_set = set(second_list)
third_set = first_set & second_set
third_list = list(third_set)
print(first_list)
print(second_list)
print(third_list)
