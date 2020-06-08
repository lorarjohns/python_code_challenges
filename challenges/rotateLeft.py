'''
Given an array a of n integers and a number, d, perform d left rotations
on the array. Return the updated array to be printed as a single line of
space-separated integers.
'''

def rotateLeft(arr, d):
    if d > len(arr):
        d = d % len(arr)
    
    return arr[d:] + arr[:d]


if __name__ == "__main__":
    print(rotateLeft([1,2,3,4,5], 6))
'''
    23451
    34512
    45123
    51234
    12345
'''