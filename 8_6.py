"""
CCI 8.6 Towers of Hanoi
"""


class Tower:
    def __init__(self, state=None):
        self.state = state if state else []

    def push(self, disc):
        self.state.append(disc)

    def pop(self):
        return self.state.pop()

    def peek(self):
        try:
            return self.state[-1]
        except IndexError:
            # In this case the list is empty, but we don't want to error.
            return None

    def __str__(self):
        return str(self.state)


def hanoi(num_disks):
    towers = [Tower(), Tower(), Tower()]

    [towers[0].push(i) for i in range(num_disks, 0, -1)]
    print("START 1: {} | 2: {} | 3: {}".format(towers[0], towers[1], towers[2]))

    def step(disc, origin, destination, buffer):
        print("\tINTER 1: {} | 2: {} | 3: {}".format(towers[0], towers[1], towers[2]))
        if disc <= 0:
            return

        step(disc-1, origin, buffer, destination)

        top = origin.pop()
        destination.push(top)

        step(disc-1, buffer, destination, origin)

    step(num_disks, towers[0], towers[2], towers[1])
    print("END 1: {} | 2: {} | 3: {}".format(towers[0], towers[1], towers[2]))


for disc in range(1, 5):
    hanoi(disc)