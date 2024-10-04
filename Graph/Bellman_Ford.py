import math


class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    
    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))
        
        
    def Bellman_Ford(self, s):
        dp = {v: math.inf for v in self.vertices}
        dp[s] = 0
        
        for i in range(len(self.vertices)-1):
            for edge in self.edges:
                start, end, weight = edge[0], edge[1], edge[2]
                if dp[end] > dp[start] + weight:
                    dp[end] = dp[start] + weight
        
        for u, v, weight in self.edges:
            if dp[v] > dp[u]+weight:
                print("Negative cycle detected")
                print()
        
        return dp

g = Graph(['A', 'B', 'C', 'D', 'E'])
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('B', 'E', 3)
g.add_edge('C', 'B', 1)
g.add_edge('C', 'D', 4)
g.add_edge('C', 'E', 5)
g.add_edge('E', 'D', 1)


dist = g.Bellman_Ford('A')   

print("Vertex Distance from Source")
for v in g.vertices:
    print("{0}\t\t{1}".format(v, dist[v]))
