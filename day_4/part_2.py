import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
map = [list(s) for s in lists]

rows = len(map)
cols = len(map[0])
dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]


def is_roll(i,j):
    if i < 0 or i >= rows:
        return False
    if j < 0 or j >= cols:
        return False
    return True if map[i][j] == '@' else False

def can_access(i,j):
    global map
    total = 0
    for dir in dirs:
        if total == 4:
            return False
        if is_roll(i+dir[0], j+dir[1]):
            total += 1
    if total < 4:
        map[i][j] = "."
        return True
    return False

result = 0

while True:
    removed = 0
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == '@':
                removed += 1 if can_access(i,j) else 0
    if removed == 0:
        break
    result += removed

print(result)
