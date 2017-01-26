"""

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

number = 100

sum_of_squares = lambda n: (n * (2 * n + 1) * (n + 1)) / 6

sum_and_square = lambda n: (n * (n + 1) * 0.5) ** 2

print(sum_and_square(number) - sum_of_squares(number))
