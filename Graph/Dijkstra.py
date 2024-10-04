import collections
import heapq
import math


class Graph():
    def __init__(self):
        self.adjacency_list = collections.defaultdict(list)
        self.MST = collections.defaultdict(list)
    
    
    def add_edge(self, start, end, weight):
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))
        
        
    def dijkstra_sssp(self, s):
        V = list(self.adjacency_list.keys())
        d = [math.inf for i in range(len(V))]
        pq = []
        for v in V:
            heapq.heappush(pq, v)
            
        d[s] = 0
        while pq:
            v = heapq.heappop(pq)
            for edge in self.adjacency_list[v]:
                neighbor, weight = edge[0], edge[1]
                if d[neighbor] > d[v]+weight:
                    d[neighbor] = d[v]+weight
                    
        print(f"Shortest distance from {s} to each vertex is:")
        for i in range(len(d)):
            print(f"{s}-{i}:{d[i]}")