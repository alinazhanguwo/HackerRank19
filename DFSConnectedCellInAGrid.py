# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def withinBound(m, n, M, N):
    if m in range(0,M) and n in range(0,N):
        return True
    else:
        return False

def DFS(m,n,grid,visited):
    visited[m][n] = 1
    count = 1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (m+i,n+j) != (m,n):
                if withinBound(m+i,n+j,len(grid),len(grid[0])):
                    if grid[m+i][n+j] == 1:
                        if visited[m+i][n+j] == 0:
                            count += DFS(m+i,n+j,grid,visited)
                            
    return count
    
# Complete the maxRegion function below.
def maxRegion(grid):
    M = len(grid)
    N = len(grid[0])
    # track visited grids
    visited = [[0]*N for _ in range(M)] 
    #print(visited)
    results = 0
    
    for m in range(M):
        for n in range(N):
            if grid[m][n]==1 and visited[m][n]==0:
                tmp = DFS(m,n,grid,visited)
                results = max(tmp, results)
       
    return results
    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
