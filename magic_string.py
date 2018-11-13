rules = {'a': ['e'],
         'e': ['a', 'i'],
         'i': ['a', 'e', 'o', 'u'],
         'o': ['i', 'u'],
         'u': ['a'],
         None: ['i', 'a', 'e', 'o', 'u']
         }


def generate_magic(n, node=None):
    if n == 1 and node == None:
        return len(rules) - 1
    elif n == 1:
        return len(rules[node])

    return sum((generate_magic(n - 1, letter) for letter in rules[node]))


assert (generate_magic(1) == 5)
assert (generate_magic(2) == 10)
assert (generate_magic(3) == 19)
assert (generate_magic(4) == 35)
assert (generate_magic(6) == 129)
assert (generate_magic(7) == 249)
