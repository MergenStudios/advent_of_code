# ATTENTION
# this is NOT my solution, and is 100% stolen
# from https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt64t2d/
# I struggled massively with this day, as you can see by the failed approaches
# in this folder. This solution is rather elegant imo.


from itertools import combinations, pairwise

(*red,) = map(eval, open("input.txt"))

area = lambda x, y, u, v: (u - x + 1) * (v - y + 1)

pairs, lines = [
    sorted(
        ((min(a, c), min(b, d), max(a, c), max(b, d)) for (a, b), (c, d) in P),
        key=lambda p: area(*p),
        reverse=True,
    )
    for P in (combinations(red, r=2), pairwise(red + [red[0]]))
]

print(area(*pairs[0]))

for x, y, u, v in pairs:
    for p, q, r, s in lines:
        if p < u and q < v and r > x and s > y:
            break

    else:
        print(area(x, y, u, v))
        break
