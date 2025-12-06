[Problem](https://adventofcode.com/2025/day/5)

## Part 1

Part 1 was straight forward, no tricks involved, just check every range for every number.

## Part 2

Theoretially you could update a set with every number in every range and get the length of that, except that aproach almost crashed my laptop becuase I didnt have enough ram.
The much more memory efficient / faster solution is to sort the ranges and smartly merge the ranges together if they overlap, and finally sum up all the ranges. I was too lazy to implement quicksort on my own so I just used the python builtin.
