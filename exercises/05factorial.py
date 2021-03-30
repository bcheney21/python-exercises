# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#

def factorial(number):
  product = 1
  for i in range(1, number + 1):
    product *= i
  
  print(product)

factorial(5)