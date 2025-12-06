import sys
from tkinter import Label


# merges two ranges, assuming they have at least *some* kind of overlap
def merge_ranges(a, b):
    merged_range = a
    # Case #1: the start is in the range and the end out side
    # update the end of the existing range
    if (a[0] <= b[0] <= a[1]) and (a[1] < b[1]):
        merged_range[1] = b[1]

    # case #2: the end is the range and the start is outside
    elif (a[0] <= b[1] <= a[1]) and (b[0] < a[0]):
        merged_range[0] = b[0]

    # b is entirely larger than a
    elif b[0] <= a[0] <= a[1] <= b[1]:
        merged_range = b

    return merged_range


with open(sys.argv[1]) as f:
    lines = f.readlines()

delimieter_pos = lines.index("\n")

ranges = [
    list(map(lambda x: int(x), line.split("-"))) for line in lines[0:delimieter_pos]
]

# sort (might implement myself later)
sorted_ranges = sorted(ranges, key=lambda x: x[0])
len_sorted_ranges = len(sorted_ranges)
merged_ranges = [sorted_ranges[0]]

sorted_pointer = 0

while sorted_pointer < len_sorted_ranges:
    # a the existing range, b is the new one
    a, b = (
        merged_ranges[-1],
        sorted_ranges[sorted_pointer],
    )

    # no merging needs to happen, append the new source to the
    # merged sources and move over one
    if a[1] < b[0]:
        merged_ranges.append(b)
        sorted_pointer += 1
        continue

    merged_ranges[-1] = merge_ranges(a, b)
    sorted_pointer += 1

# a bis b inclusive amount b - a + 1
print(sum([range[1] - range[0] + 1 for range in merged_ranges]))

# Sort ranges
#   --> https://en.wikipedia.org/wiki/Quicksort
# (0) Set window to (0, 1)
# (1) Try to merge the two elements in the window
#   --> break if window_end is > len(list)
#   (a) Sucess: delete the now redundante element, leave window the same, go to (1)
#   (b) Fail: Move window over once
#
# Possibly much better if I move the corrected ranges to a new list
# and maintain "pointers" to the list indicies
