from pathlib import Path

input_file = Path("./21/2/input")

horizontal = 0
depth = 0
aim = 0

with input_file.open("r") as file:
    for line in file.readlines():
        direction, velocity = line.strip().split(' ')
        velocity = int(velocity)
        if direction == "forward":
            depth += (aim * velocity)
            horizontal += velocity
        elif direction == "up":
            aim -= velocity
        else:
            aim += velocity

solution_part_one = horizontal * depth
print(f"{solution_part_one = }")
