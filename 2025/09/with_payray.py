# attempt 3

import itertools
import sys

import pyray


def get_area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)


with open(sys.argv[1]) as f:
    tiles = [tuple(int(x) for x in line.split(",")) for line in f.readlines()]

# get me teh list of points in the order they are connected in to form the polygon

tiles_sorted_y = sorted(tiles, key=lambda x: (x[1], x[0]))
hor_forward = {k: v for k, v in zip(tiles_sorted_y[::2], tiles_sorted_y[1::2])}
hor_backward = {v: k for k, v in hor_forward.items()}
hor_connections = {**hor_forward, **hor_backward}

tiles_sorted_x = sorted(tiles)
vert_forward = {k: v for k, v in zip(tiles_sorted_x[::2], tiles_sorted_x[1::2])}
vert_backward = {v: k for k, v in vert_forward.items()}
vert_connections = {**vert_forward, **vert_backward}

# for every point
# try to make the horizontal connection, if not get the vertical connectoin
polygon = [tiles[0]]
while len(polygon) != len(tiles):
    next_hor_point = hor_connections[polygon[-1]]
    if next_hor_point not in polygon:
        polygon.append(next_hor_point)
    else:
        polygon.append(vert_connections[polygon[-1]])

largest_area = 0
points = []
tiles_len = len(list(itertools.combinations(tiles, 2)))
num = 0
for t1, t2 in itertools.combinations(tiles, 2):
    num += 1
    if num % 100 == 0:
        print(f"{num:<5} / {tiles_len:<5}")
    corners = [t1, (t1[0], t2[1]), (t2[0], t1[1]), t2]
    # print(f"t1: {t1}, t2: {t2}, corners: {corners}")

    check = all(
        list(
            map(
                lambda x: pyray.check_collision_point_poly(x, polygon, len(polygon)),
                corners,
            )
        )
    )

    # check if all the corners are in the polygon
    # check = inside_polygon(horizontal_lines, vertical_lines, t1)

    if not check:
        # print(f"skipped {t1}, {t2}")
        # print()
        continue
    # else:
    #     print(f"accepted {t1}, {t2}")
    #     print()

    area = get_area(t1, t2)
    if area > largest_area:
        largest_area = area
        points = [t1, t2]

print(largest_area, points)


# 4631146730 is too high
