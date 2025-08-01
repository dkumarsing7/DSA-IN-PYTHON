def add_edge(matrix, i, j, w):
    if matrix[i][j] == 0:
        matrix[i][j] = w
        matrix[j][i] = w

def display_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
V = 3
matrix = [[0]*V for _ in range(V)]

add_edge(matrix, 0, 1, 4)
add_edge(matrix, 0, 2, 5)
add_edge(matrix, 1, 0, 9)
add_edge(matrix, 1, 1, 1)
add_edge(matrix, 2, 1, 9)

display_matrix(matrix)