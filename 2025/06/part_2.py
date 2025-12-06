import sys
from bdb import Breakpoint


def split_many(s, chars):
    split_s = []
    buffer = s[0]
    for char in s[1:]:
        if char in chars:
            split_s.append(buffer)
            buffer = char
            continue

        buffer += char
    split_s.append(buffer)
    return split_s


with open(sys.argv[1]) as f:
    lines = f.readlines()

operators = [
    [(operator[0], len(operator) - 1)] for operator in split_many(lines[-1], ["+", "*"])
]
del lines[-1]

problems = [[] for i in range(len(operators))]
for line in lines:
    line = line.replace("\n", "")

    index = 0
    for num_column, info in enumerate(operators):
        problems[num_column].append(line[index : index + info[0][1]])
        index += info[0][1] + 1


total = 0
for info, problem in zip(operators, problems):
    operator = info[0][0]
    match operator:
        case "+":
            subtotal = 0
            for i in range(1, info[0][1] + 1):
                column_num = ""
                for num in problem:
                    char = num[-i]
                    if char != " ":
                        column_num += char

                subtotal += int(column_num)

            print(f"+ subtotal {subtotal}")
            total += subtotal

        case "*":
            subtotal = 1
            for i in range(1, info[0][1] + 1):
                column_num = ""
                for num in problem:
                    char = num[-i]
                    if char != " ":
                        column_num += char

                subtotal *= int(column_num)

            print(f"* subtotal {subtotal}")
            total += subtotal


# get the maximum number length


print(f"Total: {total}")
