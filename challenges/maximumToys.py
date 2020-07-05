import heapq


def maximumToys(prices, k):    
    heapq.heapify(prices)
    toys = 0
    
    while k > 0:
        p = heapq.heappop(prices)
        if p > k:
            return toys
        else:
            toys += 1
            k -= p
    return toys


if __name__ == "__main__":
    prices = [1, 2, 3, 4]
    k = 7
    prices = [1, 12, 5, 111, 200, 1000, 10]
    k = 50
    prices = [33324560, 77661073, 31948330, 21522343, 97176507, 5724692, 24699815, 12079402, 6479353, 28430129, 42427721, 57127004, 26256001, 29446837, 65107604, 9809008, 65846182, 8470661, 13597655, 360]
    k = 100000
    print(maximumToys(prices, k))

