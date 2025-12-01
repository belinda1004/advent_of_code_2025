import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

dials = [(-1 if a[0] == 'L' else 1,int(a[1:]))  for a in lists]
cur = 50

zeros = 0

for dial in dials:
    cur = cur + dial[0] * dial[1]
    while cur > 99:
        cur = cur - 100
    while cur < 0:
        cur = cur + 100
    if cur == 0:
        zeros += 1

print (zeros)
