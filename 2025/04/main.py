import sys

CREATE_ANIMATION = True
ANIMATION_FRAME = 0


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


def create_animation_frame(field):
    global ANIMATION_FRAME

    dimension = len(field[0]) - 2
    with open(f"./animation/{ANIMATION_FRAME}.ppm", "wb") as f:
        f.write(b"P6\n")
        f.write(f"{dimension} {dimension}".encode("ascii"))
        f.write(b"255\n")

        ANIMATION_FRAME += 1


# int main(int argc, char **argv) {
#     if (argc != 2) {
#        printf("Wrong number of arguments: %d", argc);
#        return 1;
#     }

#     FILE *f = fopen("./out.ppm", "wb");
#     int w = 100;
#     int h = 100;


#     fprintf(f, "P6\n");
#     fprintf(f, "%d %d\n", w, h);
#     fprintf(f, "255\n");

#     for (int y = 0; y < h; y++) {
#         for (int x = 0; x < w; x++) {
#             fputc(0x00, f);
#             fputc(0xFF, f);
#             fputc(0x00, f);
#         }
#     }


#     fclose(f);
# }
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

    if replace and CREATE_ANIMATION:
        # crate animation frame if replace is true
        pass

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
