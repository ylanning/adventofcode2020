from puzzle_input import inputs

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
# Each letter tells you which half of a region the given seat is in. Start with the whole list of rows;
# the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127).
# The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
#
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
#
# F and L represent 0 (Lower half)
# B and R represent 1 (Upper half)

# Plane Layout
# - 128 rows (numbered 0-127)
# - 8 columns per row (numbered 0-7)
# - Total seats: 128 × 8 = 1,024 seats


def find_highest_seat_id(boarding_pass):
    max_seat_id = 0

    for line in boarding_pass.strip().split('\n'):
        print(line)
        # skip empty lines
        if not line.strip():
            continue

        # Replace F and L to 0, and B and R to 1
        mapping_seat = (
            line.strip()
            .replace("F", "0")
            .replace("L", "0")
            .replace("B", "1")
            .replace("R", "1")
        )

        # The first 7 characters are for row 0 -127
        row = int(mapping_seat[:7], 2)

        # The last 3 chars are for column(0-7)
        column = int(mapping_seat[7:], 2)

        """
            Binary Conversion Visual
            Boarding pass: "FBFBBFFRLR"
            After conversion: "0101100101"
                              ┌─────┐┌─┐
                              │ Row ││Col│
                              └─────┘└─┘
                              0101100 101
                                 ↓     ↓
                                44     5
            
            row = int("0101100", 2)  # = 44
            column = int("101", 2)   # = 5
            seat_id = 44 * 8 + 5     # = 357
            
            Binary: 1011
                     ┌─┬─┬─┬─┐
                     │1│0│1│1│
                     └─┴─┴─┴─┘
                     │ │ │ └─ 1s place (2⁰ = 1)
                     │ │ └─── 2s place (2¹ = 2)
                     │ └───── 4s place (2² = 4)
                     └─────── 8s place (2³ = 8)
        """

        # Every seat also has a unique seat ID:
        # multiply the row by 8, then add the column
        seat_id = row * 8 + column
        max_seat_id = max(max_seat_id, seat_id)

    return max_seat_id


high_seat = find_highest_seat_id(inputs)
print(high_seat)
