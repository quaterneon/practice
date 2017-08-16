"""
CCI 8.3 Magic index
"""
import random


def random_list(min_: int, max_: int, length: int):
    return sorted(random.sample(range(min_, max_), length))

test_cases = [[0, 1, 3, 5, 6], [3, 4], random_list(0, 3, 3), random_list(0, 6, 3), random_list(-1, 6, 3),
              random_list(-2, 6, 3), [0, 0, 0, 3], [1, 1, 1, 3], random_list(0, 100, 50), random_list(0, 200, 50),
              random_list(0, 200, 50)]

print('Test Cases: {}'.format(test_cases))


def naive(input_):
    """
    Test every value.
    :param input_:
    :return:
    """
    magic = []

    for key, value in enumerate(input_):
        if key == value:
            magic.append(key)

    return magic

print("NAIVE")
for case in test_cases:
    print("{}: {}".format(case, naive(case)))


def less_naive(input_):
    """
    Complexity of this is a bit weird. Worst case is that every value in the list is a magic index, so the worst case is
    O(n). However, in an average case we only end up evaluating a tiny fraction of the actual values in the list, but
    the complexity is related to the probability that range(0, length) overlaps with the values in the input list.

    This is based on a few observations:
      1. if input_[i] > i, then no value after i can be a magic index, unless we allow duplicates. If we allow
        duplicates, then the next possible magic index is input_[i] since the list is sorted.
      2. if input_[i] < i, then we are in a part of the list that we need to search item by item
    :param input_:
    :return:
    """
    magic = []

    ind = 0

    while ind < len(input_):
        if input_[ind] == ind:
            magic.append(ind)

        ind = max(ind+1, input_[ind])

    return magic

print("LESS NAIVE")
for case in test_cases:
    print("{}: {}".format(case, less_naive(case)))
