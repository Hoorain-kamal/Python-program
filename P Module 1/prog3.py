#3. Using reduce() – Sum of List Elements
# Program to find the sum of list elements using reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Sum:", sum_of_numbers)
