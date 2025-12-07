import sys, math

lines = open(sys.argv[1]).readlines()
operators = {"+": sum, "*": math.prod}

# part 1
total_p1 = 0
for line in zip(*map(lambda x: x.split(), lines)):
    total_p1 += operators[line[-1]](map(int, line[:-1]))

# part 2
total_p2, stack, operators = 0, [], {"+": sum, "*": math.prod} # part 2
for c in list(zip(*map(lambda x: list(reversed(x)), lines)))[1:]:
    joined = "".join(c[:-1])
    if not joined.strip(): continue

    stack.append(int(joined))

    if c[-1] in operators:
        total_p2 += operators[c[-1]](stack)
        stack.clear()

print(total_p1, total_p2)