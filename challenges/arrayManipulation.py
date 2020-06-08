"""
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each of the array element
between two given indices, inclusive.

Once all operations have been performed, return the maximum value in your array.
"""

def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    # starts, ends, values = list(zip(*queries))
    for query in queries:
        start, end, val = query
        start -= 1
        arr[start] += val
        if end <= n + 1:
            arr[end] -= val
        print(arr)
    current = max = 0
    for n in arr:
        current += n
        if max < current:
            max = current
    return max


if __name__ == "__main__":

    n = 10
    queries = [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
    print(arrayManipulation(n, queries))
