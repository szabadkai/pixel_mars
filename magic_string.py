rules = {'a': ['e'],
         'e': ['a', 'i'],
         'i': ['a', 'e', 'o', 'u'],
         'o': ['i', 'u'],
         'u': ['a'],
         None: ['i', 'a', 'e', 'o', 'u']
         }

sol = {}


def _generate_magic(n, node=None):
    if n == 1 and node == None:
        return len(rules) - 1
    elif n == 1:
        return len(rules[node])

    return sum((_generate_magic(n - 1, letter) for letter in rules[node]))


def generate_magic(n):
    return _generate_magic(n) % (10 ** 9 + 7)


assert (generate_magic(1) == 5)
assert (generate_magic(2) == 10)
assert (generate_magic(3) == 19)
assert (generate_magic(4) == 35)
assert (generate_magic(5) == 68)
assert (generate_magic(6) == 129)
assert (generate_magic(7) == 249)


def magic(length):
    previous_level = [1 for i in range(5)]
    current_level = [None for _ in range(5)]

    for _ in range(length - 1):
        current_level[0] = previous_level[1] + previous_level[2] + previous_level[4] # you can get here on 3 ways (e,i,u)
        current_level[1] = previous_level[0] + previous_level[2]
        current_level[2] = previous_level[1] + previous_level[3]
        current_level[3] = previous_level[2]
        current_level[4] = previous_level[2] + previous_level[3]

        previous_level = current_level.copy()

    return sum(previous_level) % (10 ** 9 + 7)


assert (magic(1) == 5)
assert (magic(2) == 10)
assert (magic(3) == 19)
assert (magic(4) == 35)
assert (magic(5) == 68)
assert (magic(7) == 249)
assert (magic(10 ** 5) == 207617170)
