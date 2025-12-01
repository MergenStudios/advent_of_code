import sys

DEBUG_WITH_ZEROS = False

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

if DEBUG_WITH_ZEROS:
    correct_num_zeros = []
    with open("./correct_num_zeros.txt", "r") as f:
        for line in f.readlines():
            correct_num_zeros.append(int(line))

dial_position = 50
zeros_encountered = 0
for line_num, line in enumerate(lines):
    line = line.strip()

    direction = line[0]
    turns = int(line[1:])

    zeros_line = 0

    if direction == "L":
        turns *= -1

    without_mod = dial_position + turns
    new_dial = without_mod % 100

    # we passed zero
    if without_mod > 100 or without_mod < 0:
        if dial_position == 0 and new_dial == 0:
            zeros_line += (abs(turns) // 100) - 1

        # start on zero + not end on zero
        #   we pass zero only if abs(turns) > 100
        #   abs(turns) // 100 is always going to be 0 if abs(turns) < 100
        elif dial_position == 0 and new_dial != 0:
            zeros_line += abs(turns) // 100

        # start on nonzero, end on zero
        elif dial_position != 0 and new_dial == 0:
            zeros_line += abs(turns) // 100

        # nonzero start, non zero end
        else:
            # add the 100s, and a one becaue we know we passed zero
            zeros_line += abs(turns) // 100

            # if the tens cary into the positives
            if turns > 0 and ((dial_position % 100) + (abs(turns) % 100)) > 100:
                zeros_line += 1

            # if the tens cary into the negatives
            if turns < 0 and ((dial_position % 100) - (abs(turns) % 100)) < 0:
                zeros_line += 1

    # if we land on zero
    if new_dial == 0:
        zeros_line += 1

    if DEBUG_WITH_ZEROS:
        correct = correct_num_zeros[line_num]
        if zeros_line != correct:
            print(
                f"Incorrect on line {line_num}, {line}, correct: {correct}, result: {zeros_line}\ndial: {dial_position}, turns: {turns}, no_mod {without_mod}, new_dial: {new_dial}"
            )
            breakpoint()

    zeros_encountered += zeros_line
    dial_position = new_dial


print(f"Encountered {zeros_encountered} zeros.")
