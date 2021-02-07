# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-ransom-note/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)
    c = b - a 
    if (len(list(c.elements()))==0):
        results = 'Yes'
    else:
        results = 'No'
        
    print(results)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
