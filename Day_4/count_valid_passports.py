from passport_data import datas


def count_valid_passports(passports=datas):

    # split input string into individual passport block line
    passport_lists = passports.strip().split("\n\n")
    # print(passport_lists)

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_passports = 0

    for passport in passport_lists:
        fields = set()
        # replace \n with a single space
        items = passport.replace("\n", " ").split()
        # ['ecl:gry', 'pid:860033327', 'eyr:2020', 'hcl:#fffffd', 'byr:1937', 'iyr:2017', 'cid:147', 'hgt:183cm']

        for item in items:
            # split into a list and take the first element
            field = item.split(":")[0]
            fields.add(field)

        # check if required_fields is existing in fields
        if required_fields.issubset(fields):
            valid_passports += 1

    return valid_passports


print(count_valid_passports(datas))
# 200
