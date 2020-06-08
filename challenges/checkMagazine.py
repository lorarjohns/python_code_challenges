from collections import Counter

def checkMagazine(magazine, note):
    # can_replicate = set(note).issubset(set(magazine))

    m = Counter(magazine)
    n = Counter(note)
    for word, count in n.items():
        m[word] -= count
        if m[word] < 0:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    magazine = "ive got a lovely bunch of coconuts".split()
    note = "ive got some coconuts".split()

    checkMagazine(magazine, note)