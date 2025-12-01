import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
print(lists)

dials = [(-1 if a[0] == 'L' else 1,int(a[1:]))  for a in lists]
cur = 50

zeros = 0

for dial in dials:
    zeros += (dial[1] // 100)
    distance = dial[1] % 100
    pos = cur + dial[0] * distance
    if pos == 0:
        zeros += 1
    elif pos >= 100:
        zeros += 1
        pos -= 100
    elif pos < 0:
        zeros += (1 if cur > 0 else 0)
        pos += 100
    cur = pos

    # print(dial, zeros, cur)


print (zeros)
