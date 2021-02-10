# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-big-o/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from math import *

# Complete the primality function below.
def primality(n):
    if n==1:
        return 'Not prime'
    elif n==2 or n==3:
        return 'Prime'
    elif n%2==0 or n%3==0:
        return 'Not prime'
    else:
        for i in range(3, int(sqrt(n))+1, 2):
            if n%i==0:
                return 'Not prime'
    
        return 'Prime'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
