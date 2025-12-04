import sys


# usefull for debugging
def print_field(field):
    for line in field:
        for char in line:
            print(char, end="")
        print()


def print_surroundings(surroundings):
    print(
        f"{surroundings[0]}{surroundings[1]}{surroundings[2]}\n{surroundings[3]}X{surroundings[4]}\n{surroundings[5]}{surroundings[6]}{surroundings[7]}"
    )


# takes in a padded field and returns
# the amount of paper stacks which are acessible
def count_acessible(field, replace=False):
    count = 0
    num_rows = len(field) - 1
    num_columns = len(field[0]) - 1
    for y in range(1, num_rows):
        line = field[y]
        for x in range(1, num_columns):
            # note: slices from [x:y] include x but not y
            surrounding = [
                *field[y - 1][x - 1 : x + 2],
                field[y][x - 1],
                field[y][x + 1],
                *field[y + 1][x - 1 : x + 2],
            ]

            if surrounding.count("@") <= 3 and line[x] == "@":
                if replace:
                    field[y][x] = "."
                count += 1
    return count


field = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        line = list(line.strip())

        line.insert(0, ".")
        line.append(".")

        field.append(line)

num_rows, num_columns = (
    len(field),
    len(field[0]) - 2,
)

# pad the input data
field.insert(0, list("." * (num_columns + 2)))
field.append(list("." * (num_columns + 2)))

p1_total = count_acessible(field)

p2_total = 0
p2_curr = count_acessible(field, replace=True)
while p2_curr > 0:
    p2_total += p2_curr
    p2_curr = count_acessible(field, replace=True)

print(f"part 1: {p1_total}, part 2: {p2_total}")
