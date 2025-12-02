[Problem](https://adventofcode.com/2025/day/2)

## Part 1

Instead of iterating through every number and checking if its a mirror number, I've opted for generating all invalid IDs in a given range. It doesn't make much difference with the input data given but I imagine its much more efficient if really long ranges are given.
The tricky part is getting the distinction between numbers with an even number of digits and an odd number of digits right. E.g. we can skip an entire range if start and end have an odd number of digits and are below the next highest number with an even amount of digits.

## Part 2

I also opted for a generative instead of an iterative aproach (that sounds pretentious but whatever) this time. I started by thinking about how to generate all repeating with a certain number of digits. First we consider the amount of digits `d` that `n` has. The factors of `d` (excluding d itself) give us the lengths of all patterns that repeat nicely "into" a number with `d` digits.
For every pattern lenght `p`, iterating over every number with `p` digits, and repeating that number until we are left with a number that has exactly `d` digits, eventually gives us all existing repeating numbers with `d` digits.
To solve the problem we need to add some bounds checking and consider ranges that require the generation of more than one set of of repeating numbers for different numbers of digits.

## (Unofficial / Community made) Part 3

[Link to Reddit](https://www.reddit.com/r/adventofcode/comments/1pc9mrg/2025_day_2_part_3_one_single_range/)

This is about generating _all_ invalid ids from 1 to 2\*\*32, with my solution for part 2 its just a matter of plugging in the new range
The Solution is `88304989965662`
