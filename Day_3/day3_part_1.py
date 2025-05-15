from puzzle_input import input_map


map_test = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def count_trees(map: list, right_step: int, down_step: int) -> int:
    """
    Count the number of trees encountered while traversing the map.
    """
    tree_count = 0
    row, col = 0, 0

    while row < len(map):
        # first start with row 0, col 0 and check if it is a tree
        if map[row][col] == "#":
            tree_count += 1

        # Move down the map - in this case, we move down by 1 row ==> map[1]
        row += down_step
        # Move right across the map, use modulus operator to wrap around the columns
        # in this case, we move right by 3 columns ==> map[0][3] and so on
        # modulus operator note to remember: a % b always return a positive number / a value
        # in the range of 0 to b-1
        col = (col + right_step) % len(map[0])

    return tree_count


print(count_trees(input_map, 3, 1))
