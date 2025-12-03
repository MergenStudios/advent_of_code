[Problem](https://adventofcode.com/2025/day/3)

## Solution

Same solution for both parts, as part 2 is just a more general version of part 1.
We iterate through every digit in the number and through every digit in the substring (which is initialized to be zeros), and check if the new digit is higher than the one already there. An annoying edgecase I got suck on for way too long is the bounds checking to avoid updating a digit of the substring even though there are not enough digits left in the number to fill the remaining positions in the substring.
