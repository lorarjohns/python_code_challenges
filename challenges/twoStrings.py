def twoStrings(s1, s2):
    has_common = len(set(s1).intersection(set(s2))) > 0

    if has_common:
        print("YES")

    else:
        print("NO")
