
import math
import os
import random
import re
import sys


def minimumBribes(q):
    bribes = 0
    q = [x-1 for x in q]
    #print({i:n for i, n in enumerate(q, start=1)})
    for i, n in enumerate(q):
        if n-i > 2:
            return("Too chaotic")
        
        for j in range(max(0, n-1), i):
            if q[j] > n:
                bribes += 1
    return bribes


def print_minimumBribes(q):
    bribes = 0
    q = [x-1 for x in q]
    for i, n in enumerate(q):
        if n-i > 2:
            print("Too chaotic")
            return

        for j in range(max(0, n-1), i):
            if q[j] > n:
                bribes += 1
    print(bribes)


if __name__ == "__main__":

    q = [2, 1, 5, 3, 4]
    print(minimumBribes(q))

    q = [2, 5, 1, 3, 4]
    print(minimumBribes(q))

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    print(minimumBribes(q))