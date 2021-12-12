from pathlib import Path
from typing import Dict, List
from enum import Enum, auto

input_file = Path("./21/3/input")

sorted_bits: Dict[int, list] = dict()

# part one
with input_file.open("r") as file:
    lines = file.readlines()
    for line in lines:
        for k, char in enumerate(line.strip()):
            try:
                sorted_bits[k].append(int(char))
            except KeyError:
                sorted_bits[k] = list()
                sorted_bits[k].append(int(char))

epsilon_rate_str = str()

for n, bit_block in sorted_bits.items():
    bit_block_length = len(bit_block)
    num_ones = sum(bit_block)
    num_zeros = bit_block_length - num_ones
    if num_ones >= num_zeros:
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

class DecodeMethod(Enum):
    MOST = auto()
    LEAST = auto()

def decode_rating(input: List[str], decode_method: DecodeMethod, n: int=0):
    if len(input) == 1:
        rating = int(input[0].strip(), 2)
        print(f"decode_oxygen_generator_rating finished on {n = }")
        return rating
    else:
        zeros = list()
        ones = list()

        for index, line in enumerate(input):
            bit = int(line[n])
            if bit > 0:
                ones.append(input[index])
            else:
                zeros.append(input[index])

        if decode_method == DecodeMethod.MOST:
            if len(ones) >= len(zeros):
                return decode_rating(ones, decode_method, n+1)
            else:
                return decode_rating(zeros, decode_method, n+1)
        elif decode_method == DecodeMethod.LEAST:
            if len(ones) < len(zeros):
                return decode_rating(ones, decode_method, n+1)
            else:
                return decode_rating(zeros, decode_method, n+1)

oxygen_generator_rating = decode_rating(lines, decode_method=DecodeMethod.MOST)
co2_scrubber_rating = decode_rating(lines, decode_method=DecodeMethod.LEAST)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(f"{life_support_rating = }")
