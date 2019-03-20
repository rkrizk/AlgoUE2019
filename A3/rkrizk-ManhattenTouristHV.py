#!/usr/bin/python3
import sys

matrix_list = []
row_list = []
row = " "
# read STDIN and convert to matrix[col[row[]]]
for line in sys.stdin:
    if line.startswith("G"):
        continue
    elif line == "---\n":
        matrix_list.append(row_list)
        row_list = []
    else:
        for char in line:
            if char == " " and row[-1] == " ":
                continue
            if char == "\n":
                row = row.strip("\n")
                row = row.strip(" ")
                row_list.append(row.split(" "))
                row = " "
            else:
                row += char

G_down = matrix_list[0]
G_right = matrix_list[1]
edge_length = len(G_down[0])

# check input matrices
for i in range(edge_length-1):
    if len(G_down[i]) != edge_length:
        print("G_down matrix corrupted?")

for i in range(edge_length):
    if len(G_right[i]) != edge_length-1:
        print("G_right matrix corrupted?")

matrix = [[0]]
# initialize first row and column of matrix
for i in range(edge_length-1):
    matrix[0].append(round(matrix[0][i]+float(G_right[0][i]), 2))

for i in range(edge_length-1):
    matrix.append([round(matrix[0][i]+float(G_down[i][0]), 2)])

# fill matrix horizontally
for row in range(1, edge_length):
    for col in range(1, edge_length):
        matrix[row].append(max(round(matrix[row-1][col]+float(G_down[row-1][col]), 2),
                               round(matrix[row][col-1]+float(G_right[row][col-1]), 2)))

# for i in range(edge_length):
#     print(matrix[i])

print(matrix[-1][-1])
