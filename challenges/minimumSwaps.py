
import math
import os
import random
import re
import sys

'''
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements.
You need to find the minimum number of swaps required to sort the array in ascending order.
'''

def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        # stay at this index until it contains the correct number
        while i+1 != arr[i]:
            n = arr[i]
            # put the out-of-order element in its correct index
            arr[i], arr[n-1] = arr[n-1], arr[i]
            swaps += 1
    return swaps


if __name__ == "__main__":
    print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))