from puzzle_input import inputs

def count_yes_answers(answers:str) -> int:
    # count the total number of unique 'yes' answers for all groups

    groups = answers.strip().split('\n\n')
    all_count = 0

    for group in groups:
        # Get all unique letters from the group
        unique_answers = set()

        # check each person's answer in the group
        for person in group.split('\n'):
            unique_answers.update(person.strip())

        # count unique_answers for each group
        group_count = len(unique_answers)
        all_count += group_count

    return all_count


result = count_yes_answers(inputs)
print(result)
