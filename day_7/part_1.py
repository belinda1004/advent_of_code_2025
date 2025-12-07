import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]


cols = len(lists[0])
beams = [0 for i in range(cols)]
start = lists[0].index("S")
beams[start] = 1

total = 0

for l in lists[1:]:
    new_beams = [0 for i in range(cols)]
    for i in range(cols):
        if l[i] == "^":
            if beams[i] == 1:
                total += 1
                if i > 0:
                    new_beams[i-1] = 1
                if i < cols - 1:
                    new_beams[i + 1] = 1
        elif beams[i] == 1:
            new_beams[i] = 1
    beams = new_beams

print(total)
