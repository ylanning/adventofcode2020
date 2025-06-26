from puzzle_input import password_policies

passwords = [
    ("1", "13", "r", "gqdrspndrpsrjfjx"),
    ("5", "16", "j", "jjjjkjjzjjjjjfjzjjj"),
    ("1", "16", "r", "rrrnrrrrrcnrgxrr"),
    ("1", "3", "k", "bkktwhgktv"),
]


# Each policy describes two positions in the password
# Selection Sort
def matching_index_letter(password: list) -> int:
    """
    Check if the letter at the given index matches the letter in the password.
    """
    valid_passwords_count = 0

    for policy in password:
        min_index, max_index, letter, password = policy
        min_index = int(min_index) - 1
        max_index = int(max_index) - 1
        if max_index <= len(password):
            # The letter must appear at exactly one of the two positions, not both or neither
            if (password[min_index] == letter) ^ (password[max_index] == letter):
                valid_passwords_count += 1
    return valid_passwords_count


print(matching_index_letter(password_policies))
