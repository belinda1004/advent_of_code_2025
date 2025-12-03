import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

def max_joltage_in_bank(batteries, count):
    if count == 0:
        return max(batteries)
    tens = max(batteries[:-count])
    tens_index = batteries.index(tens)
    return tens * (10 ** count) + max_joltage_in_bank(batteries[tens_index+1 :], count - 1)

result = 0
for bank in lists:
    batteries = [int(i) for i in bank]
    result += max_joltage_in_bank(batteries, 12 - 1)
print(result)
