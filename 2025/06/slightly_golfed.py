import sys, math

lines = open(sys.argv[1]).readlines()
total, stack, operators = 0, [], {"+": sum, "*": math.prod}
for c in list(zip(*map(lambda x: list(reversed(x)), lines)))[1:]:
    joined = "".join(c[:-1])
    if not joined.strip(): continue

    stack.append(int(joined))

    if c[-1] in operators:
        total += operators[c[-1]](stack)
        stack.clear()

print(total)