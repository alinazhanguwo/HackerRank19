# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem


'''
unit test:
1
4 4
1 2
2 3
3 4
2 4
1
'''

class Graph(object):
    def __init__(self, n):
        self.num_nodes = n
        self.path_list = [[] for _ in range(n)]
    
    def connect(self, start_node, end_node):
        self.path_list[start_node].append(end_node)
        self.path_list[end_node].append(start_node)
        
    def find_all_distances(self, start):
        path = [start]
        distance = [-1]*self.num_nodes
        distance[start] = 0
        WEIGHTS = 6
        
        while path:
            # remove the 1st item from list
            cur = path.pop(0)
            # check all possibilities
            for i in self.path_list[cur]:
                if distance[i] == -1:
                    path.append(i)
                    distance[i] = distance[cur] + WEIGHTS
        
        for i in range(self.num_nodes):
            if i != start:
                print(distance[i], end=" ")
        print("")

    
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    #print(graph.path_list)
    
    s = int(input())
    # n: num of nodes
    # m: num of edges
    # s: starting node
    graph.find_all_distances(s-1)
