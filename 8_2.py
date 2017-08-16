"""
CCI 8.2 Robot Grid
"""
import numpy


def find_naive_path(grid):
    """
    :param grid: Assuming numpy array of bools, where True indicates that the robot can enter the cell.
    O(2^(wh)), since we iterate over every cell and branch twice per iteration
    :return:
    """
    height = grid.shape[0]
    width = grid.shape[1]

    def eval_step(x, y):
        """
        Recursive!
        :param x:
        :param y:
        :return:
        """
        if x >= width or y >= height:
            return False, []

        if [x, y] == [height-1, width-1]:
            return True, []

        right_valid, path = eval_step(x, y+1)

        if right_valid:
            return True, [(x, y)] + path

        down_valid, path = eval_step(x+1, y)

        if down_valid:
            return True, [(x, y)] + path

        return False, []

    path_found, path = eval_step(0, 0)
    return path_found, path + [(height-1, width-1)]

print(find_naive_path(numpy.array([[True, False], [True, True]])))
print(find_naive_path(numpy.array([[True, True, False], [True, False, False], [True, True, True]])))


def find_path_memo(grid):
    """
    :param grid: Assuming numpy array of bools, where True indicates that the robot can enter the cell.
    O(wh) in time and space, since we do iterate over every grid, but we never repeat an iteration.
    :return:
    """
    height = grid.shape[0]
    width = grid.shape[1]
    path = [[None] * width] * height

    def eval_step(x, y):
        """
        Recursive!
        :param x:
        :param y:
        :return:
        """
        if x >= width or y >= height:
            return False, []

        if [x, y] == [height-1, width-1]:
            path[x][y] = []
            return True, []

        if path[x][y] is not None:
            return bool(path[x][y]), path[x][y]

        right_valid, path_section = eval_step(x, y+1)

        if right_valid:
            path[x][y] = [(x, y)] + path_section
            return True, [(x, y)] + path_section

        down_valid, path_section = eval_step(x+1, y)

        if down_valid:
            path[x][y] = [(x, y)] + path_section
            return True, [(x, y)] + path_section

        path[x][y] = []
        return False, []

    path_found, path = eval_step(0, 0)
    return path_found, path + [(height-1, width-1)]

print(find_path_memo(numpy.array([[True, False], [True, True]])))
print(find_path_memo(numpy.array([[True, True, False], [True, False, False], [True, True, True]])))
