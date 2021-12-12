from os import device_encoding
from pathlib import Path
from pprint import pprint
from typing import Dict

input_file = Path("./21/3/input")

sorted_bits: Dict[int, int] = dict()

# part one
with input_file.open("r") as file:
    lines = file.readlines()
    for n, line in enumerate(lines):
        for k, char in enumerate(line.strip()):
            try:
                sorted_bits[k].append(int(char))
            except KeyError:
                sorted_bits[k] = list()
                sorted_bits[k].append(int(char))

epsilon_rate_str = str()

for n, bit_block in sorted_bits.items():
    print(bit_block)
    bit_block_length = len(bit_block)
    num_ones = sum(bit_block)
    num_zeros = bit_block_length - num_ones
    if num_ones > num_zeros:
        epsilon_rate_str += "1"
    else:
        epsilon_rate_str += "0"

epsilon_rate = int(epsilon_rate_str, 2)
gamma_rate_str = str()

for char in epsilon_rate_str:
    if int(char) == 1:
        gamma_rate_str += "0"
    else:
        gamma_rate_str += "1"

gamma_rate = int(gamma_rate_str, 2)

print(f"{epsilon_rate_str=}, {epsilon_rate=}, {gamma_rate_str=}, {gamma_rate}")

power_consumption = epsilon_rate * gamma_rate
print(f"{power_consumption = }")

# part two
oxygen_generator_rating = 0
co2_scrubber_rating = 0
life_support_rating = oxygen_generator_rating * co2_scrubber_rating
