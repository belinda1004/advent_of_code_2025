import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
numbers = [list(map(int, line.split())) for line in lists[:-1]]
operators = lists[-1].split()

# print(numbers)
# print(operators)

result = 0

for i in range(len(operators)):
    if operators[i] == '*':
        r = 1
        for j in range(len(numbers)):
            r *= numbers[j][i]
    else:
        r = 0
        for j in range(len(numbers)):
            r += numbers[j][i]
    result += r

print(result)