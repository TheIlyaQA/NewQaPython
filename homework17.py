def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def sort_columns(matrix):
    transposed = transpose(matrix)
    for row in transposed:
        row.sort()
    return transpose(transposed)

matrix = [['a', 'c', 'e'],
          ['f', 'b', 'a'],
          ['a', 'n', 'k'],
          ['e', 'l', 'i']]

sorted_matrix = sort_columns(matrix)

for row in sorted_matrix:
    print(row)
