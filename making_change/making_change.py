#!/usr/bin/python

import sys


def making_change(amount, denominations, is_sorted=False):

    if not is_sorted:
        denominations.sort(reverse=True)

    count = 0
    if amount == 0:
        return 1
    for d in denominations:
        if d == 1:
            # stop when reach 1c
            count += 1
        else:
            for i in range(1, int(amount / d) + 1):
                if amount > d * i:
                    newAmount = amount - d * i
                    newDenoms = [x for x in denominations if x < d]
                    count += making_change(newAmount, newDenoms, True)
                elif amount == d * i:
                    count += 1

    return count


print(making_change(10, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
