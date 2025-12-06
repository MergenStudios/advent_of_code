import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

delimieter_pos = lines.index("\n")

ranges = [
    tuple(map(lambda x: int(x), line.split("-"))) for line in lines[0:delimieter_pos]
]
ids = [int(line) for line in lines[delimieter_pos + 1 :]]

fresh_items = 0
for id in ids:
    for curr_range in ranges:
        if curr_range[0] <= id <= curr_range[1]:
            fresh_items += 1
            break


print(f"Found {fresh_items} fresh items")
