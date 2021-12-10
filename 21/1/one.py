from pathlib import Path

input_file = Path("./1/input")
previous_depth = None
increments = 0
decrements = 0
with input_file.open("r") as file:
    for line in file.readlines():
        current_depth = int(line)
        if previous_depth is not None:
            if current_depth > previous_depth:
                increments += 1
            else:
                decrements += 1
        previous_depth = current_depth

print(f"{increments=}, {decrements=}")
