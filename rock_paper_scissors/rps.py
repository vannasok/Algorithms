#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps = ['rock', 'paper', 'scissors']

    if n == 0:
        return [[]]
    result = []
    for hand in rps:
        children = rock_paper_scissors(n-1)
        result += [[hand] + children[i] for i in range(0, pow(3, n - 1))]
    return result


print(rock_paper_scissors(1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
