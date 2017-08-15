"""
CCI 8.1 Triple Step
"""


def count_ways_naive(steps: int):
    """
    Naive implementation, O(3^n) seeing as it branches three ways in the middle there
    :param steps:
    :return:
    """
    def count_step(n: int):
        """
        :param n: int, steps remaining
        :return:
        """
        if n < 0:
            # off the top of the staircase
            return 0
        elif n == 0:
            # from last step only one way to get to the top
            return 1

        return count_step(n-1) + count_step(n-2) + count_step(n-3)

    return count_step(steps)


print(count_ways_naive(2))  # should be 2
print(count_ways_naive(3))  # should be 4
print(count_ways_naive(10))  # 274
#print(count_ways_naive(100))  # I don't have the patience to let this one finish.


def count_ways_memo(steps: int):
    """
    Let's store seen values. This reduces complexity to O(n), because we short-circuit the branching. We only ever
    calculate number of ways to get from a step to the top once and re-use that value, so some branches get truncated if
    we've already seen that branch before.
    :param steps:
    :return:
    """
    # create list of Nones of appropriate length. Recursive step is a closure, so this list doesn't need to be passed to
    # each recursive call.
    seen = [None] * steps

    def count_step(n: int):
        """
        :param n: int, steps remaining
        :return:
        """
        if n < 0:
            # off the top of the staircase
            return 0
        elif n == 0:
            # from last step only one way to get to the top
            return 1

        if seen[n-1]:
            return seen[n-1]

        ways = count_step(n-1) + count_step(n-2) + count_step(n-3)

        seen[n-1] = ways
        # print(n, seen)  # It's fun to watch this get populated
        return ways

    return count_step(steps)

print(count_ways_memo(2))  # should be 2
print(count_ways_memo(3))  # should be 4
print(count_ways_memo(10))  # 274
print(count_ways_memo(100))  # 180396380815100901214157639