"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?
"""

# Find which colored bags can contain which other colored bags, given above rules. I need to find how many different bag colors can eventually contain
# at least specific bag
from puzzle_input import inputs

bag_rules_test = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

def parse_bag_rules(rules: str) -> dict:
    rules_dict = {}

    for line in rules.strip().split('\n'):
        if not line.strip():
            continue

        # split on bags contain
        parts = line.split(' bags contain ')
        container_color = parts[0].strip()
        contents = parts[1].strip().rstrip('.')
        # 1 bright white bag, 2 muted yellow bags

        # handle empty bags
        if 'no other bags' in contents:
            rules_dict[container_color] = {}
            continue

        contained_bags = {}
        for item in contents.split(', '):
            type_bags = item.strip().split()
            count = int(type_bags[0])
            bag_color = " ".join(type_bags[1:-1])
            # bright white
            # muted yellow bags
            contained_bags[bag_color] = count
            # {'bright white': 1, 'muted yellow bags': 2}

        rules_dict[container_color] = contained_bags

    return rules_dict


def solve_bag_rules(bag_rules:str, target_bag: str ) -> int:
    # step 1: which bags can contain each bag
    bags_allow = {}

    bag_rules_dict = parse_bag_rules(bag_rules)
    # Input: "light red bags contain 1 bright white bag, 2 muted yellow bags."
    # Output: {'light red': {'bright white': 1, 'muted yellow': 2}}

    for container, contents in bag_rules_dict.items():
        for contained_bag in contents.keys():
            if contained_bag not in bags_allow:
                bags_allow[contained_bag] = []
            bags_allow[contained_bag].append(container)
            # {'bright white': ['light red', 'dark orange'], 'muted yellow': ['light red', 'dark orange']}

    # Find all bags that can contain the target bag
    visited = set()
    queue = [target_bag]

    while queue:
        current_bag = queue.pop(0)  # "shiny gold" -> remove first index from the queue

        if current_bag in bags_allow: # bags_allow["shiny gold"] = ["bright white", "muted yellow"]`
            for container in bags_allow[current_bag]:
                # ["bright white", "muted yellow"]
                if container not in visited:
                    visited.add(container)  # {"bright white", "muted yellow"}
                    queue.append(container) # ["bright white", "muted yellow"]

    # Excluding the target bag
    return len(visited)



if __name__ == "__main__":
    solve = solve_bag_rules(inputs, "shiny gold")
    print(solve)
