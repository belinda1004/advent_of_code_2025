import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]

rows = len(lists)
cols = len(lists[0])
dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]


def is_roll(i,j):
    if i < 0 or i >= rows:
        return False
    if j < 0 or j >= cols:
        return False
    return True if lists[i][j] == '@' else False

def can_access(i,j):
    total = 0
    for dir in dirs:
        if total == 4:
            return False
        if is_roll(i+dir[0], j+dir[1]):
            total += 1
    return total < 4

result = 0
for i in range(rows):
    for j in range(cols):
        if lists[i][j] == '@':
            result += 1 if can_access(i,j) else 0

print(result)
