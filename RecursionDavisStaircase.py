# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
options = {1:1, 2:2, 3:4}
def stepPerms(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        if (n-1) not in options.keys():
            options[n-1] = stepPerms(n-1)
        if (n-2) not in options.keys():
            options[n-2] = stepPerms(n-2)
        if (n-3) not in options.keys():
            options[n-3] = stepPerms(n-3)
        
        return options[n-1]+options[n-2]+options[n-3]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
