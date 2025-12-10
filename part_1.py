import itertools
from collections import Counter
import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

def read_line(line):
    parts = line.split(" ")
    lights = [i for i, c in enumerate(parts[0][1:-1]) if c == '#']
    # joltages = list(map(int, parts[-1][1:-1].split(",")))
    buttons = [list(map(int, b[1:-1].split(","))) for b in parts[1:-1]]
    # print(lights, joltages, buttons)
    return lights, buttons


def bingo(lights, buttons):
    # print(lights, buttons)
    count = Counter(buttons)
    total_length = max(max(lights), max(buttons)) + 1
    for i in range(total_length):
        if i in lights:  # expect to be on
            if count[i] % 2 == 0:
                return False
        else:  # expect to be off
            if count[i] % 2 == 1:
                return False
    return True


def merge(buttons):
    return [b for bs in buttons for b in bs]

def process_line(line):
    lights, buttons = read_line(line)
    r = 1
    while True:
        for c in itertools.combinations_with_replacement(buttons, r):
            bs = merge(c)
            if bingo(lights, bs):
                return r
        r += 1

result = 0

for line in lists:
    result += process_line(line)

print(result)


