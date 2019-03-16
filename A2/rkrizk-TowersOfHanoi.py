#!/usr/bin/python3
import sys
import argparse


"""
Arguments
"""

parser = argparse.ArgumentParser(description='Towers of Hanoi algorithm')

parser.add_argument('-n', type=float, dest='number',
                    help='amount of disks on first peg')

debug = False

# return --help if no arguments are passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()
if debug:
    print('Towers of Hanoi algorithm started with arguments:\n{}\n'.format(args))


def hanoi_towers(n, from_peg, to_peg):
    global counter
    if n == 1:
        counter += 1
        print("Move disk from peg {} to peg {}".format(from_peg, to_peg))
        return
    unused_peg = 6 - from_peg - to_peg
    hanoi_towers(n - 1, from_peg, unused_peg)
    counter += 1
    print("Move disk from peg {} to peg {}".format(from_peg, to_peg))
    hanoi_towers(n - 1, unused_peg, to_peg)
    return


"""
Main
"""

number = args.number
counter = 1
if number > 0 and number % 1 == 0:      # positive integer
    number = int(number)
    hanoi_towers(number, 1, 3)
    sys.stderr.write("Steps: " + str(counter) + "\n")
else:
    print("Please input a positive integer.")
