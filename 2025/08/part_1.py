import sys, math, itertools

def get_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

with open(sys.argv[1]) as f:
    boxes = {i: tuple([int(num) for num in line.split(",")]) for i, line in enumerate(f.readlines())}

# set up every  
boxes_to_circuits = {point_value: point_key for point_key, point_value in boxes.items()}
circuits = [[point_key] for point_key in boxes.keys()]
distances = []

# compute all distances of pairs
for a, b in list(itertools.combinations(boxes.values(), 2)):
    dist = get_dist(a, b)
    distances.append((dist, a, b))

# sort distances so we can iterate over them starting from the cosest 2 boxes
distances = sorted(distances, key = lambda x: x[0])

# go through the closest 10 / 10_000 (depending on the input) pairs of boxes
for dist, a, b in distances[:int(sys.argv[2])]:
    print(f"matching {a} and {b} ({dist})")
   
    # merge the b list into the a list
    b_circuit_index = boxes_to_circuits[b]
    a_circuit_index = boxes_to_circuits[a]
   
    # do nothing if the two boxes are already part of the circuit.
    # Skipping to the next one *still* means that the elves use a cable
    # because we are essentially iterating "for the fist 10k cables"
    if b_circuit_index == a_circuit_index:
        print(f"{a} and {b} already in the same circuit, skipping")
        continue

    # merge both into one circuit, clear the b circuit and update b
    # to reference the new circuit its now a part of
    b_circuit_list = circuits[b_circuit_index]
    print(f"merging circuit {b_circuit_index}: {b_circuit_list} into {a_circuit_index}: {circuits[a_circuit_index]}")
    circuits[a_circuit_index].extend(b_circuit_list)

    for point_in_old_circuit in circuits[b_circuit_index]:
        boxes_to_circuits[boxes[point_in_old_circuit]] = a_circuit_index

    circuits[b_circuit_index].clear()
    
    print()
    
# sort the circuits by size
circuits = sorted(circuits, key = lambda x: len(x), reverse = True)

result = [len(circuit) for circuit in circuits[:3]]

print(result, math.prod(result))
# 12 is th wrong answer
# 5040 is too low


# how big are the three largest circuits multiplied together

# for every number
# while len(points) > 0:
#     lowest_distance = 1_000_000_000
#     point = None
#     point_index = None
#     for a_i, a in enumerate(points.values()):
#         for b_i, b in enumerate(points.values()):
#             print(b_i, b)
#             if a == b:
#                 continue
            
#             dist = get_dist(a, b)
#             if b_i == 1:
#                 point = b
#                 point_index = a_i
#                 lowest_distance = dist
            
#             if dist < lowest_distance:
#                 point = b
#                 point_index = a_i
#                 lowest_distance = dist
                
#     try:
#         del points[point_index]
#     except KeyError as e:
#         print(f"caught key error: {e}")
#         print(points)
#         pass
    
# breakpoint()
        


   
# input: 
# the inputs are 3d coordinates
# we want to connect the two closest points
# 
# we the want to connect the next two points which are not already
# *directly* connected
# 
# if two boxes are already in the same circuit, *do not* connect them
# --> we need to be able to check if two circuits are in the same circuit
# --> buckets of circuits, and map of boxes to circuits
# 
# iterate over all points
#   get distance to each other point
#   store as distance, point a, point b
#   sort that list