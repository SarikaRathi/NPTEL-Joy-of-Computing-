# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:43:40 2021

@author: ADMIN
"""

# Week 4: Programming Assignment 1 - Factorial
# Write a program that takes a number as input and prints its factorial as output
n=int(input())
fact=1
for i in range(1,n+1):
  fact=fact*i
print(fact,end="")

# Week 4: Programming Assignment 2 - Multiples
# Given a list of n integers, count the number of integers in the list that are either a multiple of 3 or a multiple of 5. (All the numbers are guaranteed to be distinct).

# Input Format:
# Single line of input contains a list of space separated integers 
# Output Format:
# Print the count of numbers that are divisible either by 3 or 5
l=[int (x) for x in input().split()]
count=0
m=len(l)
for i in range(0,m):
  if (l[i]%3==0 & l[i]%5==0):
    count=count+1
  elif (l[i]%5==0):
    count=count+1       
print(count,end="")

# Week 4: Programming Assignment 3 - Arrangements
# Week 4: Programming Assignment 3 - Arrangements
# Given a list of binary numbers (0s and 1s), determine the number of possible arrangements of distinct binary sequences using given 0s and 1s.
# Input Format:
# Single line of input containing 0s and 1s
# Output Format:
# Print an integer value indicating the number of possible arrangements using given 0s and 1s

import math
n = input().split()
ans = math.factorial(len(n))//(math.factorial(n.count("1"))*math.factorial(n.count("0")))
print(ans,end="")



