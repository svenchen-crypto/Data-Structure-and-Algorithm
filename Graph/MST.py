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
        
            
    def prim_MST(self):
        
        vertices = list(self.adjacency_list.keys())
        root = vertices[0]
        
        #Initialize keys, priority queues and empty tree
        keys = [math.inf for _ in range(len(vertices))]
        pred = [-1 for _ in range(len(vertices))]
        pq = []
        for v in vertices:
            heapq.heappush(pq, v)
            
        keys[root] = 0
        self.MST[root] = (-1, -1)
        while pq:
            v = heapq.heappop(pq)
            for edge in self.adjacency_list[v]:
                neighbor, weight = edge[0], edge[1]
                if neighbor in pq and weight < keys[neighbor]:
                    keys[neighbor] = weight
                    pred[neighbor] = v
                    
        for i in range(1, len(vertices)):
            self.MST[keys[i]].append((pred[i], i))
        

    def kruskal_MST(self):
        pass
        
        
    def print_MST(self):
        print("MST:")
        for w, e in self.MST.items():
            if isinstance(e, tuple):
                continue
            print(f"weight:{w}, edge:{e}")
        
    