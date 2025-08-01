def add_edge(i, j, w):
    if i not in Graph:
        Graph[i] = []
    if j not in Graph[i]:
        Graph[i].append([j,w])
    if j not in Graph:
        Graph[j] = []
    if i not in Graph[j]:
        Graph[j].append([i,w])

def display_Adj_List():
    for key, values in Graph.items():
        print(f'{key} ------> {values}')

Graph = {}
add_edge(0, 1, 3)
# add_edge(1, 0, 3)
add_edge(0, 1, 6)
add_edge(0, 2, 7)
add_edge(1, 2, 7645)
add_edge(1, 2, 56)
add_edge(2, 0, 45)
display_Adj_List()