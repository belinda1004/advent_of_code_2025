import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

def max_joltage_in_bank(bank):
    batteries  = [int(i) for i in bank]
    tens = max(batteries[:-1])
    tens_index = batteries.index(tens)
    return tens * 10 + max(batteries[tens_index+1 :])

result = 0
for bank in lists:
    result += max_joltage_in_bank(bank)
print(result)
