"""
8.4 Power Set
"""

test_cases = [{'a', 'b'}, {'a', 'b', 'c'}, {'a', 'b', 'c', 'd'}]


def build_sets(case):
    """
    O(n*2^n). For each item iter over sets we've built so far.
    :param case:
    :return:
    """
    sets = [set()]

    for item in case:
        new_sets = []

        for ps in sets:
            new_set = set(ps)
            new_set.add(item)
            new_sets.append(new_set)

        sets += new_sets

    return sets


for case in test_cases:
    print('{}: {}'.format(case, build_sets(case)))


def bit_mask(case):
    """
    O(n*2^n). For each item iter over sets we've build so far.
    :param case:
    :return:
    """
    ordered = list(case)
    fill = len(case)
    num_sets = 2**(len(case))

    sets = []

    for mask in range(0, num_sets):
        bit_arr = [int(char) for char in "{:b}".format(mask).zfill(fill)]
        new_set = set()

        for ind, val in enumerate(bit_arr):
            if val:
                new_set.add(ordered[ind])

        sets.append(new_set)

    return sets


for case in test_cases:
    print('{}: {}'.format(case, bit_mask(case)))