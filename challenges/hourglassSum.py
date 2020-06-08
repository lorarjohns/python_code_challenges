#!/bin/python3

'''
Usage: hourglassSum.py FILE [options]

Arguments:
    FILE    input file

Options:
    -d DIR  --dir=DIR  input dir  [default: tests/2d-array-testcases/input]
'''
from docopt import docopt
import math
import os
import random
import re
import sys
import numpy as np
from numpy.core.numeric import zeros_like


def hourglassSum(arr):
    '''
    @param arr: array input of size n x n, n=6
       containing integers

    Returns the maximum hourglass sum in arr.

    An hourglass is a 3 x 3 subset of values
       with the values of the first and third
       columns of the second row masked out.
    '''

    sums = []

    width = arr.shape[1]-3+1
    length = arr.shape[0]-3+1

    mask = [[True, True, True],
            [False, True, False],
            [True, True, True]]

    for i in range(width):
        for j in range(length):
            sub = arr[i:i+3, j:j+3]
            hg = np.where(mask, sub, zeros_like(sub))
            sums.append(hg.sum())

    return max(sums)


def read_from_file(fp):
    with open(fp, "r") as f:
        arr = []
        for line in f.readlines():
            line = line.strip('\n')
            line = line.split()
            line = [int(x) for x in line]
            arr.append(line)

        arr = np.array(arr)
    return arr


def hourglassSum_nonumpy(arr):
    '''
    @param arr: array input of size n x n, n=6
       containing integers

    Returns the maximum hourglass sum in arr.

    This is the obnoxious version that hackerrank
    requires in which numpy is not allowed.
    '''

    sums = []

    width = 4
    length = 4

    mask = [[1, 1, 1],
            [0, 1, 0],
            [1,1,1]]
    
    for i in range(width):
        for j in range(length):
            sub = [row[j:j+3] for row in arr[i:i+3]]
            print(sub)
            agg = sum(sub[0]) + sum(sub[2]) + sub[1][1]
            sums.append(agg)
    return max(sums)


if __name__ == "__main__":

    args = docopt(__doc__)
    print(args)

    arr = read_from_file(os.path.join(args['-d'], args['FILE']))
    print(hourglassSum(arr))