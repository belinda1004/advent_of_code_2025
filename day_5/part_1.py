import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
print(lists)

# print(ranges)

fresh = []
result = 0
i = lists.index("")
ranges = [tuple(int(n) for n in l.split('-')) for l in lists[:i]]
ids = [int(l) for l in lists[i+1:]]
# print(ranges)
# print(ids)

for id in ids:
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            result += 1
            break

print(result)
