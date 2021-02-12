# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-lonely-integer/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findLonely function below.
def findLonely(arr):
    return sum(set(arr)) * 2 - sum(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = findLonely(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
