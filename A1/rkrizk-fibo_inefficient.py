#!/usr/bin/python3
import sys
import argparse

"""
Arguments
"""

parser = argparse.ArgumentParser(description='calculate Fibonacci numbers the inefficient way')

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
    print('exponential Fibonacci algorithm started with arguments:\n{}\n'.format(args))


def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    else:
        a = fibonacci(number-1)
        b = fibonacci(number-2)
        c = a+b
        f_list_inefficient.append(c)
        return c


"""
Main
"""

number = args.number
if number > 0 and number % 1 == 0:      # positive integer
    number = int(number)
    f_list_inefficient = [1, 1]
    f_list_efficient = [1, 1]
    fibonacci(number)
    for i in range(2, number):          # linear fibonacci algorithm for index list
        f_list_efficient.append(f_list_efficient[i-1] + f_list_efficient[i-2])

    if args.all:
        for i in range(0, number - 1):
            print(f_list_inefficient[f_list_efficient[i]], end=", ")  # linear fibonacci list as index
        print(f_list_inefficient[-1])
    else:
        print(f_list_inefficient[-1])

else:
    print("Please input a positive integer.")
