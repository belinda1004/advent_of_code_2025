import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

cols = len(lists[0])
start = lists[0].index("S")
times = [[0] * cols for _ in range(len(lists))]

def timeline(i, j):
    if i < 0 or i >= len(lists) or j < 0 or j >= cols:
        return 1

    if times[i][j] != 0:
        return times[i][j]

    if lists[i][j] != "^":
        return timeline(i+1, j)

    # splitter
    times[i][j] = timeline(i, j-1) + timeline(i, j+1)
    return times[i][j]

total = timeline(0, start)
print(total)
