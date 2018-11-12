from collections import Counter


def sort_intersect(m, f):
    l = Counter(m) & Counter(f) # Convenient Hash-map wrapper intersection
    r = []
    for k, v in sorted(l.items(), reverse=True): # Sorted by the key
        r += [k] * v

    return r


print(sort_intersect([1, 2, 3, 500, 700, 7000, 13000], [6, 1, 2, 7, 9, 3000, 7000, 13000]))
