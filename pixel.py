from math import sqrt

colors = {'Black': (0, 0, 0),
          'White': (255, 255, 255),
          'Red': (255, 0, 0),
          'Green': (0, 255, 0),
          'Blue': (0, 0, 255)}

def closest_color(s):
    assert(len(s) == 24)
    assert(all([i == '1' or i == '0' for i in s]))
    r, g, b = [int(i, 2) for i in [s[:8], s[8:16], s[16:]]]
    m = min(calc_distances(r, g, b).items(), key=lambda x: x[1])
    return m[0]


def calc_distances(r, g, b):
    d = {}

    for k, color in colors.items():
        d[k]=sqrt(sum([(c - c_) ** 2 for c_, c in zip((r, g, b), color)]))

    return d

# print(closest_color('200000000010000000000010'))
# print(closest_color('00000000010000000000010'))
print(closest_color('100000000000000011000010'))
print(closest_color('000000000000000000000010'))
print(closest_color('100000001110000011000010'))
