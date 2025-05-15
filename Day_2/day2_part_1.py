from puzzle_input import password_policies

# The password policy indicates the lowest and highest number of times a given letter
# must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times


# Example password policies
# passwords = [
#     ("1", "13", "r", "gqdrspndrpsrjfjx"),
#     ("5", "16", "j", "jjjjkjjzjjjjjfjzjjj"),
#     ("14", "16", "r", "rrrnrrrrrcnrgxrr"),
#     ("1", "3", "k", "bkktwhgktv"),
# ]


def is_valid_password(password_policies: list) -> int:
    valid_password = 0
    for policy in password_policies:
        letter_count = {}
        print("policy", policy)
        min_count, max_count, letter, password = policy
        for l in password:
            if l not in letter_count:
                letter_count[l] = 0
            letter_count[l] += 1
        print("letter_count", letter_count)
        count = letter_count.get(letter, 0)
        if int(min_count) <= count <= int(max_count):
            print("valid password")
            valid_password += 1
    return valid_password


def is_valid_password_with_count(password_policies: list) -> int:
    valid_password = 0
    for policy in password_policies:
        min_count, max_count, letter, password = policy
        count = password.count(letter)

        if int(min_count) <= count <= int(max_count):
            valid_password += 1
    return valid_password


print(is_valid_password(password_policies))
# print(is_valid_password_with_count(password_policy))
