import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

i = lists.index("")
ranges = sorted([tuple(int(n) for n in l.split('-')) for l in lists[:i]])

# print(ranges)

result = 0
right = -1

for r in ranges:
    left = max(right + 1, r[0])
    right = max(right, r[1])
    result += max(0, right - left + 1)
print(result)