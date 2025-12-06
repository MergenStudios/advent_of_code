import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

problems = [[operator] for operator in lines[-1].split()]
del lines[-1]

for line in lines:
    for pos, num in enumerate(line.split()):
        int_num = int(num)

        problems[pos].append(int_num)


total = 0
for problem in problems:
    operator = problem[0]
    match operator:
        case "+":
            subtotal = sum(problem[1:])
            print(f"+ {problem[1:]}, subtotal {subtotal}")
            total += subtotal

        case "*":
            subtotal = 1
            for num in problem[1:]:
                subtotal *= num

            print(f"* {problem[1:]}, subtotal {subtotal}")
            total += subtotal

print(total)
