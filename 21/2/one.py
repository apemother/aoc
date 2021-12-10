from pathlib import Path

x = 0
y = 0

input_file = Path("./2/input")
with input_file.open("r") as file:
    for line in file.readlines():
        direction, velocity = line.strip().split(' ')
        velocity = int(velocity)
        if direction in ("forward"):
            x += velocity
        elif direction == "up":
            y -= velocity
        else:
            y += velocity

print(f"{x=}, {y=} {x*y=}")
