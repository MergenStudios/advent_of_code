import sys, copy


replace = {".":0, "S": 1}
replacer = replace.get

with open(sys.argv[1]) as f:
    lines = [
        [replacer(char, char) for char in line.strip()]
        for line in f.readlines()
    ]

splits = 0
field_height = len(lines)
line_len = len(lines[0])

for line_pos in range(1, field_height):
    for char_pos in range(line_len):
        prev_char = lines[line_pos - 1][char_pos]
        cur_char = lines[line_pos][char_pos]
        
        if isinstance(prev_char, int) and prev_char > 0:
            if cur_char == "^":
                lines[line_pos][char_pos - 1] += prev_char
                lines[line_pos][char_pos + 1] += prev_char
                splits += 1
            else:
                lines[line_pos][char_pos] += prev_char
                
            
    
num_timelines = sum(lines[-1])
print(splits, num_timelines) 