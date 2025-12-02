import sys

with open(sys.argv[1]) as f:
    inp = f.readline()

ranges = inp.strip().split(",")

invalid_codes = []
for range in ranges:
    start, stop = range.split("-")
    int_start, int_stop = int(start), int(stop)
    start_len = len(start)

    mirror_start = None
    if start_len % 2 == 0:
        mirror_start = int(start[: start_len // 2])
    else:
        mirror_start = 10**start_len

        # ignore cases where both numbers have an odd number of digits
        # and are both below the next number with an even amount of digits
        # --> there are no mirror numbers in that range
        if int_start < mirror_start and int_stop < mirror_start:
            # print("skipped range without mirror numbers")
            continue

        str_mirror_start = str(mirror_start)
        mirror_start = int(str_mirror_start[: len(str_mirror_start) // 2])

    print(start, stop, mirror_start)

    # count up from mirror start, generate the mirror number and
    # check if we havent overshot yet, break if we have
    mirror_first_part = mirror_start
    mirror_number = int(str(mirror_first_part) * 2)
    new_invalid_codes = []
    while mirror_number <= int_stop:
        # ignore numbers below the range because I was a little lazy
        # on the first part
        if mirror_number >= int_start:
            new_invalid_codes.append(mirror_number)

        mirror_first_part += 1
        mirror_number = int(str(mirror_first_part) * 2)

    # print(
    #     f"Found {new_invalid_codes} invalid codes, stopped checking at {mirror_number}\n"
    # )
    invalid_codes.extend(new_invalid_codes)


print(f"found {len(invalid_codes)} invalid codes, sum: {sum(invalid_codes)}")

# approach
# instead of iterating and trying to find the numbers which are mirrors,
# I will try to generate them
# Notes
# - ranges are inclusive
# - Mirror numbers always have an even number of digits
#
# The lower and upper bounds for our mirror numbers are given by the range,
# but its the smallest mirror number that exists that is >= to the start
# and <= to the end
#
# - start at the next even-digit number starting from the input, if the input is an odd
#   9 - 340, next even digit number: 10
#   - n digit even number, 10 ** n
#
# - if its an even digit number, start at
#   - the first half, as an int?
#   - the second half, as an int?
#
#   - start at the first part + 1 if the second part is larger
#       - might be too complicated, just start the first part for now
#
# - start generating mirror numbers, check if they are in the range
# and add them to the count
#
# 1022-4568 -
#
