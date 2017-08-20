"""
CCI 8.5 Recursive multiply positive integers
"""

test_cases = [(1, 1), (1, 2), (1, 0), (1, 100), (100, 1), (20, 20), (21, 20)]


def naive(case):
    """
    Recursively add. Slightly reduce number of recursions by taking advantage of the fact that order doesn't matter.
    O(n) where n is the smaller of the two inputs.
    :param case:
    :return:
    """
    counter = min(case)
    add = max(case)

    def step(count, iter):
        if count == 0:
            #print(iter)
            return 0

        return add + step(count - 1, iter+1)  # This would recurse infinitely for negative ints

    return step(counter, 0)


for case in test_cases:
    print("{}: {}".format(case, naive(case)))


def a_bit_more_clever(case):
    """
    Bitshifting. O(log(n)), where n is the smaller of the two inputs, as we generally keep dividing in half.
    :param case:
    :return:
    """
    counter = min(case)
    add = max(case)

    def step(count, iter):

        if count == 0:
            #print(iter)
            return 0

        if count % 2 == 0:
            return step(count/2, iter+1) << 1

        return add + step(count-1, iter+1)

    return step(counter, 0)


for case in test_cases:
    print("{}: {}".format(case, a_bit_more_clever(case)))
