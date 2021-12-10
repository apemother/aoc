import math
from pathlib import Path

input_file = Path("./1/input")
increments, decrements, equals = 0, 0, 0
previous_depth = None
with input_file.open("r") as file:
    lines = file.readlines()

    for n in range(len(lines)):
        start, stop = n, n+3
        current_window = lines[start:stop]
        current_depth = sum([int(line.strip()) for line in current_window])
        print(f"{n=} {current_window=} {current_depth=}")
        if previous_depth is not None:
            if current_depth > previous_depth:
                increments += 1
            elif current_depth == previous_depth:
                equals += 1
            else:
                decrements += 1
        previous_depth = current_depth

print(f"{increments=}, {decrements=}, {equals=}")
