"""
CCI 8.6 Towers of Hanoi
"""


class Tower:
    def __init__(self, state=None):
        self.state = state if state else []

    def push(self, disc):
        self.state.append(disc)

    def pop(self):
        self.state.pop()

    def peek(self):
        try:
            return self.state[-1]
        except IndexError:
            # In this case the list is empty, but we don't want to error.
            return None

