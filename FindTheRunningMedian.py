# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem


#!/bin/python3

import math
import os
import random
import re
import sys
import heapq



if __name__ == '__main__':
    n = int(input())

    a = []

    heap_min = []
    heap_max = []

    for _ in range(n):
        a_item = int(input())
        a.append(a_item)
        
        # insert new value into one of the heaps
        if not heap_max or a_item>heap_max[0]:
            heapq.heappush(heap_max, a_item)
        else:
            heapq.heappush(heap_min, -a_item)
        
        # balance two heaps
        if len(heap_max)-len(heap_min)>1:
            heapq.heappush(heap_min, -heapq.heappop(heap_max))
        elif len(heap_min)-len(heap_max)>1:
            heapq.heappush(heap_max, -heapq.heappop(heap_min))
            
        # return median
        if len(heap_max)>len(heap_min):
            print(float(heap_max[0]))
        elif len(heap_min)>len(heap_max):
            print(float(-(heap_min[0])))
        else:
            print(float((heap_max[0] - heap_min[0])/2))


    
