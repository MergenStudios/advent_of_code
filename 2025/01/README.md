[Problem](https://adventofcode.com/2025/day/1)

## Part 1
Part 1 was straight forward, and can be solved by parsing and applying the rotation, correcting the dial position using `% 100` and incremening a counter every time we end up on zero

## Part 2
Part 2 was a little harder. I spent (too much) time trying to get it to work with floor division, but kept running into annoying edge cases.
After some time I gave up, and with a bit of help by the advent of code subreddit implemented a simplified version which adds every step one by one, and increments every time it encounters a zero. This works, but it still bugged me that I wasnt able to figure out the edge cases in my previous approach.
I used the simple version (`simplified_part_2.py`) to generate a file containing the correct numbers of zeros that should be added to the count by each line. This made debugging the edge cases way easier, and I eventually landed on `part_2.py`
