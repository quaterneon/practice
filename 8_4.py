"""
8.4 Power Set
"""

test_cases = [{'a', 'b'}, {'a', 'b', 'c'}, {'a', 'b', 'c', 'd'}]


def naive(case):
    """
    O(n^2), kinda. For each item iter over sets we've built so far.
    :param case:
    :return:
    """
    sets = []

    for item in case:
        new_sets = []

        for ps in sets:
            new_set = set(ps)
            new_set.add(item)
            new_sets.append(new_set)

        new_sets.append(set(item))
        sets += new_sets

    return sets


for case in test_cases:
    print('{}: {}'.format(case, naive(case)))