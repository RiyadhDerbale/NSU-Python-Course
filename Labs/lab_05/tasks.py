"""
NSU Python — Lab 05
Functions in Practice: Arguments, Recursion, math, and List Methods

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 05 and earlier lectures.
Do not use lambda, sorted(), filter(), or map() in this lab.
"""

# ============================================================
# Task 1 — Positional and keyword arguments
# ============================================================
# Create a function:
#
#   describe_student(name, age, city)
#
# The function should print:
#   Name: ...
#   Age: ...
#   City: ...
#
# Call the function three times:
# 1. using only positional arguments;
# 2. using only keyword arguments in a different order;
# 3. using one positional argument and the rest as keyword arguments.
#
# Example:
# describe_student("Anna", 23, "Novosibirsk")
#
# Output:
# Name: Anna
# Age: 23
# City: Novosibirsk

# Write your code below:


# ============================================================
# Task 2 — Default arguments
# ============================================================
# Create a function:
#
#   shipping_cost(weight, rate=2.5)
#
# It should return:
#   weight * rate
#
# Call it:
# 1. with only weight;
# 2. with a custom rate;
# 3. with rate passed as a keyword argument.
#
# Example:
# shipping_cost(4)
# returns 10.0

# Write your code below:


# ============================================================
# Task 3 — Early return
# ============================================================
# Create a function:
#
#   safe_divide(a, b)
#
# If b is 0, return None immediately.
# Otherwise return a / b.
#
# Test:
# safe_divide(10, 2)  -> 5.0
# safe_divide(10, 0)  -> None

# Write your code below:


# ============================================================
# Task 4 — *args: total score
# ============================================================
# Create a function:
#
#   total_score(*scores)
#
# Return the sum of all scores.
#
# The function must work with any number of arguments,
# including zero arguments.
#
# Examples:
# total_score(10, 20, 30) -> 60
# total_score(5)          -> 5
# total_score()           -> 0
#
# Inside the function, scores is a tuple.

# Write your code below:


# ============================================================
# Task 5 — *args: average score
# ============================================================
# Create a function:
#
#   average_score(*scores)
#
# If no scores are given, return None.
# Otherwise return the arithmetic mean.
#
# Examples:
# average_score(80, 90, 100) -> 90.0
# average_score()             -> None

# Write your code below:


# ============================================================
# Task 6 — **kwargs: profile
# ============================================================
# Create a function:
#
#   show_profile(**details)
#
# Print each key and value in this form:
#   key: value
#
# Example call:
# show_profile(name="Anna", city="Novosibirsk", year=1)
#
# Possible output:
# name: Anna
# city: Novosibirsk
# year: 1

# Write your code below:


# ============================================================
# Task 7 — Combining fixed arguments, *args, and **kwargs
# ============================================================
# Create a function:
#
#   course_report(student, *scores, **options)
#
# It should print:
#   Student: ...
#   Scores: (...)
#   Options: {...}
#
# Example:
# course_report(
#     "Mira",
#     80, 92, 75,
#     rounded=True,
#     scale=100
# )
#
# Expected structure:
# Student: Mira
# Scores: (80, 92, 75)
# Options: {'rounded': True, 'scale': 100}

# Write your code below:


# ============================================================
# Task 8 — Scope
# ============================================================
# Create a global variable:
#
#   TAX_RATE = 0.20
#
# Create a function:
#
#   final_price(price)
#
# Inside the function:
# 1. calculate a LOCAL variable called tax;
# 2. return price + tax.
#
# Do not modify TAX_RATE.
#
# Example:
# final_price(100) -> 120.0
#
# Think about:
# - TAX_RATE is global.
# - tax exists only inside final_price().

# Write your code below:


# ============================================================
# Task 9 — Recursive countdown
# ============================================================
# Create a recursive function:
#
#   countdown(n)
#
# If n == 0:
#   print("Go!")
#   stop the function.
#
# Otherwise:
#   print n
#   call countdown(n - 1)
#
# Do NOT use a loop.
#
# Example:
# countdown(3)
#
# Output:
# 3
# 2
# 1
# Go!

# Write your code below:


# ============================================================
# Task 10 — Recursive factorial
# ============================================================
# Create a recursive function:
#
#   factorial(n)
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 1;
# - otherwise return n * factorial(n - 1).
#
# Do NOT use a loop.
#
# Examples:
# factorial(5)  -> 120
# factorial(0)  -> 1
# factorial(-2) -> None

# Write your code below:


# ============================================================
# Task 11 — Recursive sum
# ============================================================
# Create a recursive function:
#
#   sum_to(n)
#
# It should return:
#   1 + 2 + 3 + ... + n
#
# Rules:
# - if n < 0, return None;
# - if n == 0, return 0;
# - otherwise use recursion.
#
# Do NOT use a loop and do NOT use sum().
#
# Examples:
# sum_to(4) -> 10
# sum_to(0) -> 0

# Write your code below:


# ============================================================
# Task 12 — math module and list methods
# ============================================================
# Part A — math
#
# Import math.
#
# Ask the user for the radius of a circle.
# Calculate and print:
# - circumference = 2 * math.pi * radius
# - area = math.pi * radius ** 2
# - area rounded UP with math.ceil()
# - area rounded DOWN with math.floor()
#
# Example for radius 3:
# Circumference: 18.849...
# Area: 28.274...
# Area ceil: 29
# Area floor: 28
#
#
# Part B — list methods
#
# Start with:
# numbers = [10, 20, 20, 30]
#
# Perform these operations in order:
# 1. append 40
# 2. extend with [50, 60]
# 3. insert 15 at index 1
# 4. print how many times 20 appears
# 5. print the index of the first 30
# 6. remove the first 20
# 7. pop the last item and save it in removed
# 8. print numbers
# 9. print removed
#
# Do not use sorted() in this task.

# Write your code below:


# ============================================================
# Task 13 — BONUS: Recursive digit sum
# ============================================================
# Create a recursive function:
#
#   digit_sum(n)
#
# Assume n is a non-negative integer.
#
# Return the sum of its digits.
#
# Hint:
# - last digit: n % 10
# - remaining digits: n // 10
#
# Base case:
# if n < 10, return n
#
# Examples:
# digit_sum(1234) -> 10
# digit_sum(7)    -> 7
#
# Do NOT convert the number to a string.
# Do NOT use a loop.

# Write your code below:


# ============================================================
# Task 14 — BONUS: Student result summary
# ============================================================
# Create a function:
#
#   result_summary(name, *scores, passing=60)
#
# Requirements:
# - if no scores are given, return:
#     "No scores"
# - calculate the average;
# - count how many scores are >= passing;
# - return a string in this form:
#
#   "Anna: average=80.0, passed=3/4"
#
# Example:
# result_summary("Anna", 80, 70, 50, 120, passing=60)
#
# returns:
# "Anna: average=80.0, passed=3/4"
#
# Use a loop to count passed scores.
# Do not use filter() or map().

# Write your code below:


# ============================================================
# Task 15 — Function with validation
# ============================================================
# Create a function:
#
#   calculate_discount(price, discount=10)
#
# Requirements:
# - price must be greater than 0;
# - discount must be between 0 and 100.
#
# If the values are invalid, return None.
#
# Otherwise return the final price after applying the discount.
#
# Formula:
# final_price = price - price * discount / 100
#
# Examples:
# calculate_discount(100)     -> 90.0
# calculate_discount(200, 25) -> 150.0
# calculate_discount(100, 120) -> None
# calculate_discount(-20, 10)  -> None

# Write your code below:


# ============================================================
# Task 16 — Minimum and maximum with *args
# ============================================================
# Create a function:
#
#   score_range(*scores)
#
# If no scores are given, return None.
#
# Otherwise return the difference between
# the largest and smallest score.
#
# Do NOT use max() or min().
#
# Use a loop to find the smallest and largest values.
#
# Examples:
# score_range(10, 30, 20, 50) -> 40
# score_range(5)               -> 0
# score_range()                -> None

# Write your code below:


# ============================================================
# Task 17 — Count values above a limit
# ============================================================
# Create a function:
#
#   count_above(limit, *numbers)
#
# Return how many numbers are greater than limit.
#
# Examples:
# count_above(10, 5, 12, 30, 7, 20) -> 3
# count_above(100, 10, 20, 30)       -> 0
# count_above(5)                      -> 0
#
# Use a loop.

# Write your code below:


# ============================================================
# Task 18 — **kwargs: configuration
# ============================================================
# Create a function:
#
#   show_settings(**settings)
#
# If no settings are given, print:
#   No settings
#
# Otherwise print each setting:
#
#   key = value
#
# Example:
#
# show_settings(
#     language="Python",
#     version=3.12,
#     debug=True
# )
#
# Possible output:
# language = Python
# version = 3.12
# debug = True

# Write your code below:


# ============================================================
# Task 19 — math: distance between two points
# ============================================================
# Create a function:
#
#   distance(x1, y1, x2, y2)
#
# Calculate the Euclidean distance between two points.
#
# Formula:
#
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
#
# Use math.sqrt().
#
# Example:
# distance(0, 0, 3, 4) -> 5.0
#
# Import math.

# Write your code below:


# ============================================================
# Task 20 — List operations: shopping list
# ============================================================
# Start with:
#
# shopping = ["bread", "milk", "eggs"]
#
# Perform these operations in order:
#
# 1. append "rice"
# 2. insert "coffee" at index 1
# 3. extend the list with ["tea", "sugar"]
# 4. remove "milk"
# 5. print the index of "eggs"
# 6. print how many times "bread" appears
# 7. pop the last item and store it in removed_item
# 8. print the final shopping list
# 9. print removed_item
#
# Expected final list:
# ["bread", "coffee", "eggs", "rice", "tea"]

# Write your code below:


# ============================================================
# Task 21 — CHALLENGE: Recursive power
# ============================================================
# Create a recursive function:
#
#   power(base, exponent)
#
# Assume exponent is a non-negative integer.
#
# Rules:
# - if exponent == 0, return 1;
# - otherwise:
#
#     base^exponent =
#     base * base^(exponent - 1)
#
# Examples:
# power(2, 5)  -> 32
# power(3, 3)  -> 27
# power(10, 0) -> 1
#
# Do NOT use **.
# Do NOT use math.pow().
# Do NOT use a loop.

# Write your code below:


# ============================================================
# Task 22 — CHALLENGE: Recursive digit counter
# ============================================================
# Create a recursive function:
#
#   count_digits(n)
#
# Assume n is a non-negative integer.
#
# Return the number of digits in n.
#
# Examples:
# count_digits(7)     -> 1
# count_digits(1234)  -> 4
# count_digits(10000) -> 5
#
# Hint:
# Remove the last digit with:
#
#   n // 10
#
# Base case:
# if n < 10:
#     return 1
#
# Do NOT convert n to a string.
# Do NOT use a loop.

# Write your code below:


# ============================================================
# Task 23 — CHALLENGE: Recursive list sum
# ============================================================
# Create a recursive function:
#
#   recursive_sum(numbers)
#
# Return the sum of all numbers in the list.
#
# Examples:
# recursive_sum([10, 20, 30]) -> 60
# recursive_sum([5])          -> 5
# recursive_sum([])           -> 0
#
# Hint:
#
# Base case:
# if the list is empty:
#     return 0
#
# Recursive idea:
#
# first element + sum of the remaining elements
#
# Do NOT use:
# - sum()
# - for
# - while

# Write your code below:


# ============================================================
# Task 24 — CHALLENGE: Exam statistics
# ============================================================
# Create a function:
#
#   exam_statistics(student, *scores, passing=60)
#
# If no scores are provided, return:
#
#   "No scores"
#
# Otherwise calculate:
#
# - average score
# - highest score
# - lowest score
# - number of passed scores
# - number of failed scores
#
# Do NOT use:
# - min()
# - max()
# - sum()
#
# Calculate everything using a loop.
#
# Return a string like:
#
# "Anna: average=72.5, highest=90, lowest=50,
#  passed=3, failed=1"
#
# Example:
#
# exam_statistics(
#     "Anna",
#     80, 70, 50, 90,
#     passing=60
# )
#
# returns:
#
# "Anna: average=72.5, highest=90, lowest=50,
#  passed=3, failed=1"

# Write your code below:
# ============================================================
# Task 25 — Function with multiple return values
# ============================================================
# Create a function:
#
#   min_max(numbers)
#
# The function should return TWO values:
# - the smallest number
# - the largest number
#
# Do NOT use min() or max().
#
# Example:
# smallest, largest = min_max([5, 2, 9, 1, 7])
#
# smallest -> 1
# largest  -> 9
#
# Assume the list is not empty.

# Write your code below:


# ============================================================
# Task 26 — Temperature converter
# ============================================================
# Create a function:
#
#   convert_temperature(value, unit="C")
#
# If unit == "C":
#   convert Celsius to Fahrenheit.
#
# Formula:
# F = C * 9 / 5 + 32
#
# If unit == "F":
#   convert Fahrenheit to Celsius.
#
# Formula:
# C = (F - 32) * 5 / 9
#
# For any other unit, return None.
#
# Examples:
# convert_temperature(0)       -> 32.0
# convert_temperature(100)     -> 212.0
# convert_temperature(32, "F") -> 0.0
# convert_temperature(10, "K") -> None

# Write your code below:


# ============================================================
# Task 27 — Find a value manually
# ============================================================
# Create a function:
#
#   find_value(numbers, target)
#
# Return the index of the FIRST occurrence of target.
#
# If target does not exist, return -1.
#
# Do NOT use:
# - list.index()
#
# Examples:
# find_value([10, 20, 30, 20], 20) -> 1
# find_value([1, 2, 3], 5)          -> -1

# Write your code below:


# ============================================================
# Task 28 — Remove all occurrences
# ============================================================
# Create a function:
#
#   remove_all(numbers, value)
#
# Remove ALL occurrences of value from the list.
#
# Example:
#
# numbers = [10, 20, 20, 30, 20]
# remove_all(numbers, 20)
#
# numbers becomes:
# [10, 30]
#
# You may use:
# - while
# - remove()
# - count()
#
# Do NOT create a new list.

# Write your code below:


# ============================================================
# Task 29 — Recursive multiplication
# ============================================================
# Create a recursive function:
#
#   multiply(a, b)
#
# Assume:
# - a is an integer
# - b is a non-negative integer
#
# Calculate a * b using addition and recursion.
#
# Do NOT use the * operator for multiplication.
# Do NOT use loops.
#
# Idea:
#
# a * 4 = a + a + a + a
#
# Base case:
# if b == 0:
#     return 0
#
# Examples:
# multiply(5, 3)  -> 15
# multiply(10, 0) -> 0
# multiply(-2, 4) -> -8

# Write your code below:


# ============================================================
# Task 30 — Recursive Fibonacci
# ============================================================
# Create a recursive function:
#
#   fibonacci(n)
#
# Rules:
# fibonacci(0) -> 0
# fibonacci(1) -> 1
#
# For n > 1:
#
# fibonacci(n) =
#     fibonacci(n - 1) + fibonacci(n - 2)
#
# Examples:
# fibonacci(0) -> 0
# fibonacci(1) -> 1
# fibonacci(6) -> 8
#
# Do NOT use loops inside the function.

# Write your code below:


# ============================================================
# Task 31 — math: hypotenuse
# ============================================================
# Create a function:
#
#   hypotenuse(a, b)
#
# Return the length of the hypotenuse of a
# right triangle.
#
# Formula:
#
# c = sqrt(a^2 + b^2)
#
# Use math.sqrt().
#
# If a <= 0 or b <= 0:
#     return None
#
# Examples:
# hypotenuse(3, 4)  -> 5.0
# hypotenuse(5, 12) -> 13.0
# hypotenuse(-3, 4) -> None

# Write your code below:


# ============================================================
# Task 32 — Function that modifies a list
# ============================================================
# Create a function:
#
#   add_student(students, name)
#
# The function should append name to students.
#
# It should NOT return the list.
#
# Example:
#
# students = ["Anna", "Alex"]
#
# result = add_student(students, "Mira")
#
# print(students)
# print(result)
#
# Output:
#
# ['Anna', 'Alex', 'Mira']
# None
#
# Think about:
# - lists are mutable;
# - the function changes the original list;
# - a function without return returns None.

# Write your code below:


# ============================================================
# Task 33 — Return versus print
# ============================================================
# Create TWO functions:
#
#   square_print(n)
#   square_return(n)
#
# square_print(n):
# - prints n ** 2
# - does not explicitly return anything
#
# square_return(n):
# - returns n ** 2
#
# Then run:
#
# a = square_print(5)
# b = square_return(5)
#
# print(a)
# print(b)
#
# Explain the difference between the outputs.
#
# This task is especially about understanding:
#
# print(...)
#
# versus
#
# return ...

# Write your code below:


# ============================================================
# Task 34 — Empty return
# ============================================================
# Create a function:
#
#   check_age(age)
#
# If age < 0:
#     print("Invalid age")
#     return
#
# Otherwise:
#     print("Valid age")
#
# Test:
#
# result1 = check_age(-5)
# result2 = check_age(20)
#
# Print result1 and result2.
#
# Question:
# What value does the function return in both cases?
#
# Remember:
#
# return
#
# is equivalent to:
#
# return None

# Write your code below:


# ============================================================
# Task 35 — Number statistics with *args
# ============================================================
# Create a function:
#
#   number_statistics(*numbers)
#
# If no numbers are provided:
#     return None
#
# Otherwise calculate:
# - total
# - average
# - smallest
# - largest
#
# Do NOT use:
# - sum()
# - min()
# - max()
#
# Return all four values.
#
# Example:
#
# total, average, smallest, largest = \
#     number_statistics(5, 10, 2, 13)
#
# Results:
# total    -> 30
# average  -> 7.5
# smallest -> 2
# largest  -> 13

# Write your code below:


# ============================================================
# Task 36 — Recursive sum of list elements
# ============================================================
# Create:
#
#   recursive_sum(numbers)
#
# Examples:
#
# recursive_sum([1, 2, 3, 4]) -> 10
# recursive_sum([10])         -> 10
# recursive_sum([])           -> 0
#
# Use recursion only.
#
# Do NOT use:
# - sum()
# - for
# - while
#
# Hint:
#
# [1, 2, 3, 4]
#
# can be thought of as:
#
# 1 + sum([2, 3, 4])

# Write your code below:


# ============================================================
# Task 37 — Reverse a list using list methods
# ============================================================
# Create a function:
#
#   reverse_list(numbers)
#
# Reverse the list IN PLACE using:
#
#   .reverse()
#
# The function should not explicitly return anything.
#
# Example:
#
# numbers = [1, 2, 3, 4]
#
# result = reverse_list(numbers)
#
# print(numbers)
# print(result)
#
# Output:
#
# [4, 3, 2, 1]
# None

# Write your code below:


# ============================================================
# Task 38 — Math: nearest integer
# ============================================================
# Import math.
#
# Create a function:
#
#   rounding_report(number)
#
# Print:
#
# Original: ...
# Floor: ...
# Ceil: ...
#
# Example:
#
# rounding_report(4.7)
#
# Output:
#
# Original: 4.7
# Floor: 4
# Ceil: 5
#
# Test also:
#
# rounding_report(-4.7)
#
# Pay attention to how floor() behaves
# with negative numbers.

# Write your code below:
