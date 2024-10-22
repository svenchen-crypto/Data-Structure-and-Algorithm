import collections
import heapq
import math


class Graph():
    def __init__(self):
        self.adjacency_list = collections.defaultdict(list)
        self.MST = collections.defaultdict(list)
    
    
    def addEdge(self, start, end, weight):
        self.adjacency_list[start].append((end, weight))
        self.adjacency_list[end].append((start, weight))
        
    def primMST(self):
        vertices = list(self.adjacency_list.keys())
        root = vertices[0]
        # Initialize the MST
        for v in vertices:
            self.MST[v] = (-1, math.inf)
        visited = set()
        # Initialize the min heap and add the root node to it
        min_heap = []
        heapq.heappush(min_heap, (0, root))
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            visited.add(node)
            for neighbor, weight in self.adjacency_list[node]:
                # Grow the tree by one if new edge with lower weight is found
                if neighbor not in visited and self.MST[neighbor][1] > weight:
                    self.MST[neighbor] = (node, weight)
                    heapq.heappush(min_heap, (weight, neighbor))
        

    def kruskal_MST(self):
        pass
        
    def printMST(self):
        print("MST:")
        for u, (v, w) in self.MST.items():
            if w == math.inf:
                continue
            print(f"weight:{w}, edge:{(u, v)}")
        
g = Graph()
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)
g.addEdge(3, 9, 10)
g.addEdge(4, 3, 1)
g.addEdge(0, 9, 999)
g.addEdge(9, 2, 4)

g.primMST()
g.printMST()