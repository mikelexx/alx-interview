#!/usr/bin/env python3

'''
This concept is best explained by striver at youtube
[search : Rotate Matrix/Image by 90 Degrees | Brute - Optimal   [TUF]]
'''
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]
col_len =  len(matrix[0])
row_len = len(matrix)
mat2 = [[0 for _ in range(col_len)] for _ in range(row_len)]
for row in matrix:
    print(row)
print('90 degrees anticlockwise')
for col in range(col_len):
    for row in range(row_len):
        mat2[row_len -col -1][row] = matrix[row][col]
        #print(f'mat2[{row_len - col -1}][{row}] = {matrix[row][col]}')

for row in mat2:
    #print(row)
    pass
print('90 clockwise')        
for row in range(row_len):
    for col in range(col_len):
        mat2[col][col_len - row - 1] = matrix[row][col]
for row in mat2:
    pass
    #print(row)
print('rotating 90 degrees using transpose reverse method ...')    
print('\n\t1. transposed matrix')

def transpose_in_place(matrix):
    for i in range(row_len):
        for j in range(i + 1, col_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

transpose_in_place(matrix)            
for row in matrix:
    print('\t{}'.format(row))
print()
print('\t2. reverse rows of transposed matrix to get rotated matrix')
def reverse_matrix_rows_in_place(matrix):
    for i in range(row_len):
        start, end = 0, col_len - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1
        
reverse_matrix_rows_in_place(matrix)       
print()
for row in matrix:
    print('\t{}'.format(row))

