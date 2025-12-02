import sys


# return all factors of n except n itself
def get_factors(n):
    factors = []
    for potential_factor in range(1, n):
        if n % potential_factor == 0:
            factors.append(potential_factor)

    return factors


with open(sys.argv[1]) as f:
    inp = f.readline()

ranges = inp.strip().split(",")

invalid_codes = []
for given_range in ranges:
    start, stop = given_range.split("-")
    int_start, int_stop = int(start), int(stop)

    # minimum and maximum # of digits
    min_digits, max_digits = len(start), len(stop)

    range_invalid_codes = set()
    for num_digits in range(min_digits, max_digits + 1):
        # this has to be a set to avoid duplicates because
        # 2 x "1" = 1 x "11"
        mirror_numbers = set()

        # generate all repeating numbres with a specific number of digits
        factors = get_factors(num_digits)

        # for every factor (# of digits of a pattern that repeats nicely),
        for pattern_length in factors:
            # for every nuber 10**(pattern_length - 1) to 10**pattern_length
            # repeat it until num_digits is filled
            for num in range((10 ** (pattern_length - 1)), 10**pattern_length):
                mirror_num = int((num_digits // pattern_length) * str(num))

                if int_start <= mirror_num <= int_stop:
                    mirror_numbers.add(mirror_num)

        range_invalid_codes.update(mirror_numbers)

    invalid_codes.extend(range_invalid_codes)

print(f"found {len(invalid_codes)} invalid codes, sum: {sum(invalid_codes)}")

# instead of only generating mirror numbers,
# we now need to generate any number containing a repeating pattern
# e.g. 101010 is also an invalid code now
# this means we need to change our generation strategy
#
# to generate *every* possible number matching the constraints from 0 up to int_end,
# we can just count up starting at 1, and chain that number behind itself as many times
# as we can before hitting the maximum
# --> this only generates numbers which have as many digits as the maximum
#
# I can generate these stepwise, as in 1, 11, 111 etc.
# This means however, that we need to filter out other mirror numbers,
# as 2 x "11" and 4 x "1" would both yield 1111
# <a lot of thought later>
# whatever I'll just use a set
#
# only if the # of digits is 6 we have to check the repeating patterns with 3 digits,
# we always need to check 1s
# we then need to check all factors of n (with n being the # of digits) except for n itself
# --> get_factors
#
#
# is there something weird going on if our range is a
# 5 digit number to a 9 digit number?
# 9 factors to 1 and 3
# wait, we then generate all 5 digit repeating numbers, all 6 digit repeating numbers etc.
# to generate all somposite mirros of # of digits n we need the factors, to know which patterns
# can even repeat
# --> uhhh see above? I literally thought about that 2 minutes ago


# Other Idea
# can this be done done by simply counting up?
#
# is it possible to find the *next* repeating number
# well for it to repeat we need to know the factors of the # of digits
# is it possible to somehow count up smartly
