#!/usr/bin/python3
import sys
import argparse

"""
Arguments
"""

parser = argparse.ArgumentParser(description='calculate Fibonacci numbers the efficient way')

parser.add_argument('-n', type=float, dest='number',
                    help='amount of fibonacci numbers to print')
parser.add_argument('--all', action='store_true',
                    help='print all numbers to maximum number')

debug = False

# return --help if no arguments are passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()
if debug:
    print('linear Fibonacci algorithm started with arguments:\n{}\n'.format(args))

"""
Main
"""

number = args.number
if number > 0 and number % 1 == 0:      # positive integer
    number = int(number)
    fibonacci_list = [1, 1]
    for i in range(2, number):              # linear fibonacci algorithm
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])

    if args.all:
        for i in range(number - 1):
            print(fibonacci_list[i], end=", ")
        print(fibonacci_list[-1])
    else:
        print(fibonacci_list[-1])
else:
    print("Please input a positive integer.")
