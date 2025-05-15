from puzzle_input import input_map
from day3_part_1 import count_trees


def count_trees_multiple_slopes(map: list, slopes: list) -> int:
    """
    Count the number of trees encountered while traversing the map for multiple slopes.
    """
    total_tree_count = 1
    for slope in slopes:
        right_step, down_step = slope
        tree_count = count_trees(map, right_step, down_step)
        # multiplying all the tree_count together
        total_tree_count = total_tree_count * tree_count
    return total_tree_count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print(count_trees_multiple_slopes(input_map, slopes))
