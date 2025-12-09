import sys, itertools

def get_area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

with open(sys.argv[1]) as f:
    tiles = [tuple(int(x) for x in line.split(",")) for line in f.readlines()]
    
largest_area = 0
points = []
for t1, t2 in itertools.combinations(tiles, 2):
   area = get_area(t1, t2) 
   if area > largest_area:
       largest_area = area
       points = [t1, t2]
       
print(f"largest area: {largest_area}, points: {points}")