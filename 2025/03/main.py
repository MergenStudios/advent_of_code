import sys


# n: the string of digits
# l: the length of the extraced maximum voltage
def greatest_substring(digits, substr_len):
    print(f"Working with {digits}")
    substr = ["0" for _ in range(substr_len)]
    num_digits = len(digits)

    for digit_pos, digit in enumerate(digits):
        int_digit = int(digit)
        for substr_pos, substr_digit in enumerate(substr):
            # print(
            #     digit_pos,  # 0 indexed
            #     num_digits,  # 1 indexed / count
            #     substr_len,  # 1 indexed / count
            #     substr_pos,  # 0 indexed
            #     (digit_pos + 1) + ((substr_len) - (substr_pos + 1)) <= num_digits,
            # )

            # num_digits = 10, substr_len = 2
            # 0 1 2 3 4 5 6 7 8 9 <-- digits
            # 1 2 3 4 5 6 7 8 9 10 <-- one indexed positions
            # at pos 7, we can still update substr[0]
            if (
                int_digit > int(substr_digit)
                and (digit_pos + 1) + ((substr_len) - (substr_pos + 1)) <= num_digits
            ):
                substr[substr_pos] = digit

                # set all digits after substr_pos to zero
                for i in range(substr_pos + 1, substr_len):
                    substr[i] = "0"

                break

    return int("".join(substr))


with open(sys.argv[1]) as f:
    lines = f.readlines()

p1_total, p2_total = 0, 0
for line in lines:
    line = line.strip()
    p1_total += greatest_substring(line, 2)
    p2_total += greatest_substring(line, 12)

print(f"part 1 total: {p1_total}, part 2 total: {p2_total}")
