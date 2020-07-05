'''
Two strings are anagrams of each other if the letters of one string
can be rearranged to form the other string. Given a string, find the
number of pairs of substrings of the string that are anagrams of each other.
'''

from collections import Counter
from itertools import combinations

def sherlockAndAnagrams(s):
    count = 0
    combos = ["".join(sorted(s[i:j])) for i, j in combinations(range(1+len(s)), 2)]
    counter = Counter(combos)
    for item in counter:
        count += (counter[item]*(counter[item]-1))//2
        # Binomial coefficient
        # n(n-1)/2
    print(counter)
    return count


if __name__ == "__main__":

    #sherlockAndAnagrams("abcd")
    sherlockAndAnagrams("kkkk")