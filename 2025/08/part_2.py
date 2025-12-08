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
for dist, a, b in distances:
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
    
    # check if all boxes are now connected (all are in one big circuit)
    if len(circuits[a_circuit_index]) == len(boxes):
        print(a, b, a[0]*b[0])
        break
    
    print()
    