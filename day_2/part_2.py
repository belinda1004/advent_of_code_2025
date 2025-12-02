import input

# lists = input.sample
lists = input.input
lists = lists.split(",")

result = 0
ranges = [a.split("-")  for a in lists]

def f(x):
    for i in range(1, len(x) // 2 + 1):
        if len(x) % i == 0 and x[i:] == x[:-i]:
            return int(x)
    return 0


for r in ranges:
    s,e = int(r[0]), int(r[1])
    for x in range(s, e + 1):
        result += f(str(x))
print(result)



