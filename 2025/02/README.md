[Problem](https://adventofcode.com/2025/day/2)

## Part 1
Instead of iterating through every number and checking if its a mirror number, I've opted for generating all invalid IDs in a given range. It doesn't make much difference with the input data given but I imagine its much more efficient if really long ranges are given
The tricky part is getting the distinction between numbers with an even number of digits and an odd number of digits right. E.g. we can skip an entire range if start and end have an odd number of digits and are below the next highest number with an even amount of digits.
