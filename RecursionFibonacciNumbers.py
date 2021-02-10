# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem


# The beginning of Fibonacci Sequence is 0,1,1,2,3,5,8,13,21,...
stored = {}
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if n not in stored.keys():
            # store the results to eliminate redundant computation
            stored[n] = fibonacci(n-2)+fibonacci(n-1)
        return stored[n]

n = int(input())
print(fibonacci(n))
