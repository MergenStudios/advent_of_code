# attempt #2

import itertools
import sys
from pprint import pprint as pp


def get_area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)


def is_on_line(lines, p):
    for l in lines:
        if (l[0][0] <= p[0] <= l[1][0]) or (l[0][1] <= p[0] <= l[1][1]):
            # breakpoint()
            return True

    breakpoint()
    return False


def is_in_rectangle(rect, p):
    check = (rect[0][0] <= p[0] <= rect[1][0]) and (rect[0][1] <= p[1] <= rect[1][1])

    if check:
        print(f"success: {p} in {rect}")

    return check


with open(sys.argv[1]) as f:
    tiles = [tuple(int(x) for x in line.split(",")) for line in f.readlines()]

tiles_sorted_y = sorted(tiles, key=lambda x: (x[1], x[0]))
horizontal_lines = list(zip(tiles_sorted_y[::2], tiles_sorted_y[1::2]))

tiles_sorted_x = sorted(tiles)
vertical_lines = list(zip(tiles_sorted_x[::2], tiles_sorted_x[1::2]))


# get all rectangles which are spanned
# by two tiles where the rectangle is entirely
# contained within the polygon

rectangles = [
    (t1, t2)
    for t1, t2 in itertools.combinations(tiles, 2)
    # check if rectangle (t1, t2) is entirely containd in the polygon
    if all(
        [
            is_on_line([*vertical_lines, *horizontal_lines], x)
            for x in [(t1[0], t2[1]), (t1[1], t2[0])]
        ]
    )
]

print(len(list(itertools.combinations(tiles, 2))), len(rectangles))
pp(rectangles)

# for every rectangle, only update the biggest area if the points are all good
largest_area = 0
points = []
for t1, t2 in itertools.combinations(tiles, 2):
    corners = [t1, (t1[0], t2[1]), (t2[0], t1[1]), t2]
    print(f"t1: {t1}, t2: {t2}, corners: {corners}")

    # only update if all the corners are containd within the polygon,
    # meaning if all the points are containd in any of the above computed
    # rectangles
    checks = []
    for corner in corners:
        corner_check = False
        for rect in rectangles:
            if is_in_rectangle(rect, corner):
                corner_check = True
                break
            # else:
            #     print(f"{corner} not in {rect}")

        checks.append(corner_check)

    check = all(checks)

    # check if all the corners are in the polygon
    # check = inside_polygon(horizontal_lines, vertical_lines, t1)

    if not check:
        print(f"skipped {t1}, {t2}")
        print()
        continue
    else:
        print(f"accepted {t1}, {t2}")
        print()

    area = get_area(t1, t2)
    if area > largest_area:
        largest_area = area
        points = [t1, t2]

print(largest_area, points)
# first apply the rules
#
# in a line its trivial, if there is a neven numbre of red tiles
# they all get connected
# for columns this is also trivial
#
#
#
# do the same thigns again
#
#
#
# how to do a rectangle bounds check
# how to do a bounds check between polygons
#
# I can check if lines cross each other
#
# I can check if a point is inside a rectangle easily
#
# going from the left, for a point to be inside it has to cross an
# odd amount of lines. If I sort the lines by x and y position,
# and then iterate over the lines from the x and y direction,
# and check every time if the point crosses the line, and keep track of that,
# when I reach the point and I have crossed an odd number of lines for both axis
#
#
# create a rectangle
# infer the missing corners
# check if those corners are contained in polygon
#
#
# check if a point is in (or on the broder of) the polygon
#
# just use horzontal lines
# do a check what sided of the field the point is closer to
# I need to make sure I actually cross the line
#
#
