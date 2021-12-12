from pathlib import Path

input_file = Path("./21/1/input")

# part one
previous_depth = None
increments, decrements = 0, 0
with input_file.open("r") as file:
    for line in file.readlines():
        current_depth = int(line)
        if previous_depth is not None:
            if current_depth > previous_depth:
                increments += 1
            else:
                decrements += 1
        previous_depth = current_depth

solution_part_one = increments
print(f"{solution_part_one =}")

# part two
increments, decrements, equals = 0, 0, 0
previous_depth = None
with input_file.open("r") as file:
    lines = file.readlines()

    for n in range(len(lines)):
        start, stop = n, n + 3
        current_window = lines[start:stop]
        current_depth = sum([int(line.strip()) for line in current_window])
        if previous_depth is not None:
            if current_depth > previous_depth:
                increments += 1
            elif current_depth == previous_depth:
                equals += 1
            else:
                decrements += 1
        previous_depth = current_depth

solution_part_two = increments
print(f"{solution_part_two =}")
