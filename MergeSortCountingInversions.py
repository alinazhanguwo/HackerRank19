# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-merge-sort/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    n = len(arr)
    if n==1:
        return 0
    n1 = int(n/2)
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    results = countInversions(arr1) + countInversions(arr2)
    
    # 2 1 3 1 2
    # n1=2, n2=3
    # arr1 = [2,1], arr2 = [3,1,2]
    # [2,1]
    # n1=1, n2=1
    # arr1 = [2], arr2 = [1]
    # merge arr1 and arr2
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 <n1 and (i2>=n2 or arr1[i1]<=arr2[i2]):
            arr[i] = arr1[i1]
            results += i2
            i1 += 1 
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
