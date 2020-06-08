'''
Starting with a 1-indexed array of zeros and a list of operations,
for each operation add a value to each of the array element
between two given indices, inclusive.

Once all operations have been performed, return the maximum value in your array.
'''


# def arrayManipulation(n, queries):
#     max_val = 0
#     arr = [0]*n
#     for query in queries:
#         start, end, val = query
#         start -= 1
#         for i in range(start, end):
#             arr[i] += val
#             if arr[i] > max_val:
#                 max_val = arr[i]
#     return max_val


# def arrayManipulation(n, queries):
#     length = len(queries)
# 
#     max_val = current_val = 0

#     arr = [0]*(n+1)
#     for query in queries:
#         start, end, val = query
#         arr[start-1] += val
#         current_val += n
#         if end <= length:
#             arr[end] -= val
# 
#     for n in arr:
#         if current_val > max_val:
#             max_val = current_val
#     
#     return max_val

def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    # starts, ends, values = list(zip(*queries))
    for query in queries:
        start, end, val = query
        start -= 1
        arr[start] += val
        if end <= n+1:
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
    queries = [(1,5,3), (4,8,7), (6,9,1)]
    print(arrayManipulation(n, queries))
