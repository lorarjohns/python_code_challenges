'''
(1, x): insert x
(2, y): delete one occurrence of y if present
(3, z): check if int present with frequency z. if yes print 1, else 0

q: 2d array of queries q x 2

Return an integer array consisting of all the outputs of queries of type 3.
'''

from collections import Counter, defaultdict


def freqQuery(q):
    freqs = defaultdict(int)
    hist = defaultdict(int)

    result = []
    for op, n in q:
        if op == 1:
            hist[freqs[n]] = max(0, hist[freqs[n]]-1)
            freqs[n] += 1
            hist[freqs[n]] += 1

        elif op == 2:
            hist[freqs[n]] = max(0, hist[freqs[n]] - 1)
            freqs[n] = max(0, freqs[n]-1)
            if freqs[n] > 0:
                hist[freqs[n]] += 1

        elif op == 3:
            if hist[n] > 0:
                result += [1]
            else:
                result += [0]
    return result

if __name__ == "__main__":
    q = [(1, 5),
         (1, 6),
         (3, 2),
         (1, 10),
         (1, 10),
         (1, 6),
         (2, 5),
         (3, 2)]

    print(freqQuery(q))

    q = int(input().strip())