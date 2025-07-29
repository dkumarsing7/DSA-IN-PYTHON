class Graph: 
    def __init__(self):
        v = 3
        self.matrix = [[0]*v for _ in range(v)]
    
    def add_edge(self, i, j):
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def display_matrix(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 0)
g.add_edge(1, 1)
g.add_edge(2, 1)

g.display_matrix()