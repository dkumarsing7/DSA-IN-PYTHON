class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = [] 
        if destination not in self.graph[source]:
            self.graph[source].append(destination)
    
    def display_Adj_List(self):
        for key, values in self.graph.items():
            print(f'{key} ------> {values}')
        
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 1)
g.add_edge(1, 0)
g.add_edge(1, 4)
g.add_edge(1, 0)
g.display_Adj_List()
