import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()


dial_position = 50
zeros_encountered = 0
for line_num, line in enumerate(lines):
    direction = line[0]
    turns = int(line[1:])

    if direction == "L":
        turns *= -1

    new_dial = (dial_position + turns) % 100

    if new_dial == 0:
        zeros_encountered += 1

    dial_position = new_dial


print(f"Landed on {zeros_encountered} zeros.")
