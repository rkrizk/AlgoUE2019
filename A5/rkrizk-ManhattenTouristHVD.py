#!/usr/bin/python3
import sys
import argparse


"""
Arguments
"""

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                 description='Needleman-Wunsch algorithm for pairwise global sequence alignment')

parser.add_argument('--match', type=int, default=1,
                    help='Score for a match    (default: +1)')
parser.add_argument('--mismatch', type=int, default=-1,
                    help='Score for a mismatch (default: -1)')
parser.add_argument('--gap', type=int, default=-2,
                    help='Score for a gap      (default: -2)')


# return --help if no arguments are passed
# if len(sys.argv) == 1 and sys.stdin is None:
#     parser.print_help(sys.stderr)
#     sys.exit(1)

print(sys.stdin)

header = ""
sequence = ""
# read STDIN and convert FASTA class
for line in sys.stdin:
    if line.startswith(">"):
        print(header.strip())
        print(sequence.strip())
        sequence = ""
        header = line
    else:
        sequence += line.strip()

print(header.strip())
print(sequence.strip())


# def read_fasta(file):
#     seq_list = []
#     seq = ""
#     for line in sys.stdin:
#         if line.startswith('>'):
#             if not seq is "":
#                 seq_list.append(seq)
#             seq = ""
#         else:
#             seq += line.strip("\n")
#     seq_list.append(seq)
# return seq_list


# matrix_list = []
# row_list = []
# row = " "
# # read STDIN and convert to nested list
# for line in sys.stdin:
#     if line.startswith("G"):
#         continue
#     elif line == "---\n":
#         matrix_list.append(row_list)
#         row_list = []
#     else:
#         for char in line:
#             if char == " " and row[-1] == " ":
#                 continue
#             if char == "\n":
#                 row = row.strip("\n")
#                 row = row.strip(" ")
#                 row_list.append(row.split(" "))
#                 row = " "
#             else:
#                 row += char
#
# G_down = matrix_list[0]
# G_right = matrix_list[1]
# G_diag = matrix_list[2]
# edge_length = len(G_down[0])
#
# # check input matrices
# for i in range(edge_length-1):
#     if len(G_down[i]) != edge_length:
#         print("G_down matrix corrupt?")
#
# for i in range(edge_length):
#     if len(G_right[i]) != edge_length-1:
#         print("G_right matrix corrupt?")
#
# for i in range(edge_length-1):
#     if len(G_diag[i]) != edge_length-1:
#         print("G_diag matrix corrupt?")
#
# matrix = [[0]]
# # initialize first row and column of matrix
# for i in range(edge_length-1):
#     matrix[0].append(round(matrix[0][i]+float(G_right[0][i]), 2))
#
# for i in range(edge_length-1):
#     matrix.append([round(matrix[i][0]+float(G_down[i][0]), 2)])
#
# # fill matrix horizontally
# for row in range(1, edge_length):
#     for col in range(1, edge_length):
#         matrix[row].append(round(max(matrix[row-1][col]+float(G_down[row-1][col]),
#                                      matrix[row][col-1]+float(G_right[row][col-1]),
#                                      matrix[row-1][col-1]+float(G_diag[row-1][col-1])), 2))
#
# # for i in range(edge_length):
# #     print(matrix[i])
#
# print(matrix[-1][-1])
