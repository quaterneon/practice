"""
CCI 8.7 Perms without dups
"""

test_cases = ['abc', '1234', 'aaaab']


def naive(case):
    """
    O(n*n!) time.
    :param case:
    :return:
    """
    chars = set(case)

    def permute():
        if not chars:
            return set([''])

        num_chars = len(chars)
        char = chars.pop()
        perms = permute()
        new_perms = set()

        for ind in range(0, num_chars):
            for perm in perms:
                new_perms.add(perm[:ind] + char + perm[ind:])

        return new_perms

    return permute()

for case in test_cases:
    print("{}: {}".format(case, naive(case)))


def still_naive(case):
    """
    Still O(n*n!)
    :param case:
    :return:
    """
    chars = set(case)

