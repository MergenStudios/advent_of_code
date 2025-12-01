import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

GENERATE_CORRECT_COUNTS = False

zeros_per_line = []

dial_position = 50
zeros_encountered = 0
for line in lines:
    line = line.strip()

    direction = line[0]
    turns = int(line[1:])

    sign = 1
    if direction == "L":
        sign = -1

    new_zeros = 0
    for _ in range(turns):
        dial_position += sign

        # update dial position
        if dial_position == 100:
            dial_position = 0

        if dial_position == -1:
            dial_position = 99

        if dial_position == 0:
            new_zeros += 1

    zeros_encountered += new_zeros
    zeros_per_line.append(f"{new_zeros}\n")


if GENERATE_CORRECT_COUNTS:
    with open("correct_num_zeros.txt", "w") as f:
        f.writelines(zeros_per_line)


print(f"Encountered {zeros_encountered} zeros.")
