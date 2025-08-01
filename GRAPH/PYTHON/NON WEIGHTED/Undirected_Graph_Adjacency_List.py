def add_edge(i, j):
    if i not in Graph:
        Graph[i] = []
    if j not in Graph[i]:
        Graph[i].append(j)
    if j not in Graph:
        Graph[j] = []
    if i not in Graph[j]:
        Graph[j].append(i)

def display_Adj_List():
    for key, values in Graph.items():
        print(f'{key} ------> {values}')

Graph = {}
add_edge(0, 1)
add_edge(0, 1)
# add_edge(0, 2)
# add_edge(1, 2)
# add_edge(1, 2)
add_edge(2, 0)
display_Adj_List()