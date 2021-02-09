# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem


class MyQueue(object):
    def __init__(self):
        self.results = []
    
    def peek(self):
        if self.results:
            return self.results[0]
            
    def pop(self):
        if self.results:
            del(self.results[0])
        
    def put(self, value):
        self.results.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
