import itertools
from collections import Counter
import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

def read_line(line):
    parts = line.split(" ")
    # lights = [i for i, c in enumerate(parts[0][1:-1]) if c == '#']
    joltages = list(map(int, parts[-1][1:-1].split(",")))
    buttons = [list(map(int, b[1:-1].split(","))) for b in parts[1:-1]]
    # print(lights, joltages, buttons)
    return buttons, joltages


def bingo(joltages, buttons):
    # print(lights, buttons)
    count = Counter(buttons)
    total_length = len(joltages)

    for i in range(total_length):
        if count[i] != joltages[i]:
            return False
    return True


def merge(buttons):
    return [b for bs in buttons for b in bs]

def process_line(line):
    buttons, joltages = read_line(line)
    r = 1
    while True:
        for c in itertools.combinations_with_replacement(buttons, r):
            bs = merge(c)
            if bingo(joltages, bs):
                return r
        r += 1


result = 0

for line in lists:
    result += process_line(line)

print(result)


