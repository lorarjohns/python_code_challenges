'''
You are given an array and you need to find number of tripets of indices (i,j,k)
such that the elements at those indices are in geometric progression for a given
common ratio r and i < j < k.
'''
from collections import defaultdict

def countTriplets(arr, r):
    # number of three-tuples possible for each key (if found)
    three_tup = defaultdict(int)
    # number of two-tuples possible for each key (if found)
    expected = defaultdict(int)
    res = 0
    for val in arr:
        # we already found val/r and val/(r**2), so val completes the triple
        res += three_tup[val]
        # increment new two- and three-tuples:
        # if k*r is found, then (k/r, k, k*r) is a triple in the array
        three_tup[val*r] += expected[val]
        # if k*r is found, then (k, k*r) is a double in the array
        expected[val*r] += 1
    print(res)

if __name__ == "__main__":

    arr = [1, 4, 16, 64]
    countTriplets(arr, 4)
    arr = [1, 2, 2, 4]
    countTriplets(arr, 2)
    arr = [1, 3, 9, 9, 27, 81]
    countTriplets(arr, 3)
    arr = [1, 5, 5, 25, 125]
    countTriplets(arr, 5)