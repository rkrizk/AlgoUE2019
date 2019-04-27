#!/usr/bin/python3
import sys
import argparse


"""
Arguments
"""

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                 description='Needleman-Wunsch algorithm for pairwise global sequence alignment\n'
                                             'provide a multifasta file via "./rkrizk-NW.py [--options] < input.fa"')

parser.add_argument('--match', type=int, default=1,
                    help='score for a match    (default: +1)')
parser.add_argument('--mismatch', type=int, default=-1,
                    help='score for a mismatch (default: -1)')
parser.add_argument('--gap', type=int, default=-2,
                    help='score for a gap      (default: -2)')

DEBUG = False

if DEBUG is False and sys.stdin.isatty():
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()
match = args.match
mismatch = args.mismatch
gap = args.gap


"""
read multifasta
"""

if not DEBUG:
    header = ""
    sequence = ""
    fasta_dict = {}
    for line in sys.stdin:
        if line.startswith(">"):
            # print(header.strip())
            # print(sequence.strip())
            fasta_dict[header.strip()] = sequence.strip()
            sequence = ""
            header = line
        else:
            sequence += line.strip()

    # print(header.strip())
    # print(sequence.strip())
    fasta_dict[header.strip()] = sequence.strip()

    header_s = list(fasta_dict)[1]
    header_t = list(fasta_dict)[2]
    s = fasta_dict[header_s]
    t = fasta_dict[header_t]

if DEBUG:
    header_s = "NC_006551.1"
    header_t = "NC_035889.1"
    s = "CCACGGCCCG"
    t = "ACACGGGCCTG"


"""
Fill Matrix
"""

M = [[0]]

for col in range(1, len(s)+1):
    M[0].append(col * gap)

for row in range(1, len(t)+1):
    M.append([row * gap])

for row in range(1, len(t)+1):
    for col in range(1, len(s)+1):
        if s[col-1] == t[row-1]:
            p = match
        else:
            p = mismatch
        M[row].append(max(M[row-1][col] + gap,
                          M[row][col-1] + gap,
                          M[row-1][col-1] + p))

"""
Print Matrix
"""

# if len(s) < 20 and len(t) < 20:
#     print(" ", "s", sep="\t", end="\t")
#     for col in range(len(s)):
#         print(s[col], end="\t")
#
#     print("")
#     print("t", end="\t")
#     for col in range(len(s)+1):
#         print(M[0][col], end="\t")
#
#     print("")
#     for row in range(1, len(t)+1):
#         print(t[row-1], end="\t")
#         for col in range(len(s)+1):
#             print(M[row][col], end="\t")
#         print("")
#     print("")


"""
Backtrack
"""

s_new = ""
t_new = ""
clustal = ""
row = len(t)
col = len(s)

while row > 0 or col > 0:
    if s[col - 1] == t[row - 1] and M[row][col] == M[row - 1][col - 1] + match:
        s_new += s[col - 1]
        t_new += t[row - 1]
        clustal += "*"
        row -= 1
        col -= 1
    elif s[col - 1] != t[row - 1] and M[row][col] == M[row - 1][col - 1] + mismatch:
        s_new += s[col - 1]
        t_new += t[row - 1]
        clustal += " "
        row -= 1
        col -= 1
    elif M[row][col] == M[row][col-1] + gap:
        s_new += s[col-1]
        t_new += "-"
        clustal += " "
        col -= 1
    elif M[row][col] == M[row - 1][col] + gap:
        s_new += "-"
        t_new += t[row - 1]
        clustal += " "
        row -= 1
    else:
        print("Error in backtracking")
        sys.exit(2)


"""
Output Alignment
"""

s_new_rev = ""
t_new_rev = ""
clustal_rev = ""

for i in range(1, len(s_new)+1):
    s_new_rev += s_new[-i]
for i in range(1, len(t_new)+1):
    t_new_rev += t_new[-i]
for i in range(1, len(clustal) + 1):
    clustal_rev += clustal[-i]

header_len = max(len(header_s), len(header_t))
for i in range(1, 1 + round((len(s_new_rev)+29)/60)):
    print("{}".format(header_s.ljust(header_len + 5)), s_new_rev[(i-1)*60:i*60])
    print("{}".format(header_t.ljust(header_len + 5)), t_new_rev[(i-1)*60:i*60])
    print("{}".format("".ljust(header_len + 5)), clustal_rev[(i-1)*60:i*60])
    print("")

# output similarity value
sys.stderr.write(str(M[len(t)][len(s)]) + "\n")
