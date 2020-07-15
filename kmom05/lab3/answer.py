#!/usr/bin/env python3

"""
b2ac686c2804ed58014fcd12e5038270
oopython
lab3
v2
pamo18
2019-02-19 11:02:49
v3.1.3 (2018-09-13)

Generated 2019-02-19 12:02:49 by dbwebb lab-utility v3.1.3 (2018-09-13).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name
# pylint: disable=no-else-return

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - Recursion
#
# If you need to peek at examples or just want to know more, take a look at
# the page: https://docs.python.org/3/library/index.html. Here you will find
# everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Simple recursion
#
# Practice on creating recursive functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers `12` up to `39`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#
def sum_numbers(num):
    """sum"""
    if num == 39:
        return num
    else:
        return num + sum_numbers(num + 1)

res = sum_numbers(12)


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create a recursive function in the code below that calculates the sum of
# the numbers in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If its an empty list return `0`.
#
# Answer with the sum.
#
# Write your code below and put the answer into the variable ANSWER.
#
def sum_list(l):
    """sum list"""
    if l == []:
        return 0
    else:
        head = l[0]
        tail = l[1:]
        return head + sum_list(tail)

res = sum_list([4, 5, 6, 11, 9, 1, 2, 3, 8])


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a recursive function in the code below that searches a list for a
# number and returns the index of the number.
# Find the index of `2` in the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
# If the number cant be found, return -1.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#
def search_list(myList, number):
    """search list"""
    def search(l, num):
        """search"""
        tail = l[1:]
        if l[0] == num:
            return 0
        else:
            return 1 + search(tail, num)
    try:
        return search(myList, number)
    except IndexError:
        return -1


res = search_list([4, 5, 6, 11, 9, 1, 2, 3, 8], 2)


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Use the function from the previous assignment to find the number `18` in
# the list `[4, 5, 6, 11, 9, 1, 2, 3, 8]`.
#
# Answer with the index.
#
# Write your code below and put the answer into the variable ANSWER.
#

res = search_list([4, 5, 6, 11, 9, 1, 2, 3, 8], 18)


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a recursive function in the code below that calculates `12` to the
# power of `7`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
def calculate_pow(num, p):
    """pow"""
    if p == 0:
        return 1
    return num * calculate_pow(num, p - 1)

res = calculate_pow(12, 7)


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a recursive function in the code below that turns a string
# backwards. Turn the string "switcharoo" backwards.
#
# Answer with the backward string.
#
# Write your code below and put the answer into the variable ANSWER.
#
def reverse_word(word):
    """reverse word"""
    count = len(word)
    if count == 0:
        return ""
    else:
        return word[-1] + reverse_word(word[:-1])

res = reverse_word("switcharoo")


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
