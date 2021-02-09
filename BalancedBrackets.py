# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def check_balance(expression):
    while len(expression)>0:
        length_start = len(expression)
        expression = expression.replace('()','')
        expression = expression.replace('[]','')
        expression = expression.replace('{}','')
        length_end = len(expression)
        
        if length_start == length_end:
            return 'NO'
    
    return 'YES'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        print(check_balance(expression))
