[Problem](https://adventofcode.com/2025/day/6)

Honestly I was super sleep deprived I'm sure theres a better solution

## Part 1

Straight forward, the trick is to know that `.split()` without arguments splits by whitespaces (plural!) by default

## Part 2

Had to some (imo) ugly nested loops to get it to work, the thing that eventually led me down the right path was recognizing that the operator at the bottom is always left aligend, which can be used to properly align the other columns.
