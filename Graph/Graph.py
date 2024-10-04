import collections
import math

class Graph():
    def __init__(self):
        self.adjacency_list = collections.defaultdict(list)
    
    
    def add_edge(self, edges):
        for edge in edges:
            src, dest = edge[0], edge[1]
            self.adjacency_list[src].append(dest)
            self.adjacency_list[dest].append(src) #skip this line if you want a directed graph


    '''BFS implementation, return a list store distance from source node to each node'''       
    def BFS(self, s) -> list:
        distance = [math.inf for i in range(len(self.adjacency_list.keys())+1)]
        #print(distance)
        queue = collections.deque()
        visited = set()
        
        queue.append(s)
        visited.add(s)
        distance[s] = 0
        
        while(queue):
            curr_vertex = queue.pop()
            for node in self.adjacency_list[curr_vertex]:
                if node in visited:
                    continue
                queue.append(node)
                visited.add(node)
                distance[node] = distance[curr_vertex]+1
        
        return distance[1:]
    

    # Driver method 
    def DFS(self) -> None:
        visited = set()
        for v in self.adjacency_list.keys():
            # If v is undiscovered, apply dfs to it
            if v not in visited:
                self.DFS_util(v, visited) #search v and its neighbors
                      
               
    def DFS_util(self, src, visited) -> None:
        print(f"Marking vertex {src} as visited")
        visited.add(src)
        for neighbor in self.adjacency_list[src]:
            if neighbor not in visited:
                self.DFS_util(neighbor, visited)
        
        print("Vertices visited:")
        print(visited)