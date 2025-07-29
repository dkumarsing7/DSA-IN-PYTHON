def add_edge(matrix, i, j):
    matrix[i][j] = 1
    matrix[j][i] = 1

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
V = 3
matrix = [[0]*V for _ in range(V)]

add_edge(matrix, 0, 1)
add_edge(matrix, 0, 2)
add_edge(matrix, 1, 0)
add_edge(matrix, 1, 1)
add_edge(matrix, 2, 1)

display_matrix(matrix)