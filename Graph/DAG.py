import collections

class DAG():
    def __init__(self) -> None:
        self.adjacency_list = collections.defaultdict(list)
    
    
    def add_edge(self, edges) -> None:
        for edge in edges:
            src, dest = edge[0], edge[1]
            self.adjacency_list[src].append(dest)
            
            
    # Driver method 
    def topological_sort(self):
        topological_order = []
        visited = set()
        for v in list(self.adjacency_list.keys()):
            #print(f"Visiting vertex {v}")
            if v not in visited:
                self.topologicalsort_util(v, topological_order, visited)
        return topological_order
    
    
    def topologicalsort_util(self, v, topological_order, visited):
        visited.add(v)
        for neighbor in self.adjacency_list[v]:
            if neighbor not in visited:
                self.topologicalsort_util(neighbor, topological_order, visited)
                
        #print(f"Node {v} finished")
        topological_order.insert(0, v)
        

    #DFS to compute finish times of each node
    def DFS(self, s, finished_times, visited):
        visited.add(s)
        for v in self.adjacency_list[s]:
            if v not in visited:
                self.DFS(v, finished_times, visited)
                
        finished_times.append(s)
        
    
    def transpose(self):
        g_transposed = DAG()
        vertices = self.adjacency_list.keys()
        for v in vertices:
            for neighbor in self.adjacency_list[v]:
                g_transposed.adjacency_list[neighbor].append(v)
                
        return g_transposed
    
    
    #DFS implementation to get SCC in dfs tree
    def find_one_scc(self, s, visited, scc):
        visited.add(s)
        for v in self.adjacency_list[s]:
            if v not in visited:
                scc = self.find_one_scc(v, visited, scc)
                
        scc.insert(0, s)
        return scc
    
    
    #Driver method
    def kosaraju_scc(self):
        SCCs = []
        
        #1st pass of DFS, compute finish time
        finished_times = []
        visited = set()
        vertices = list(self.adjacency_list.keys())
        
        for v in vertices:
            if v not in visited:
                self.DFS(v, finished_times, visited)
        
        #Compute transpose of dag
        g_transpose = self.transpose()
        
        #2nd pass of DFS
        visited = set()
        while finished_times:
            node = finished_times.pop()
            if node not in visited:
                scc = g_transpose.find_one_scc(node, visited, [])
                SCCs.append(scc)
            
        return SCCs
    

    def tarjan_scc(self):
        pass