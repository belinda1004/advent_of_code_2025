import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
points = [list(map(int, line.split(','))) for line in lists]

# print(points)
points = sorted(points)
# print(points)

distances = []
n = len(points)
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]
        d = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
        distances.append((i, j, (x1,y1,z1), (x2, y2, z2), d))
        # distances.append((i, j, d))

distances.sort(key=lambda x: x[4])
print(distances)

point_on_line = [None for _ in range(len(points))]
lines = []

line_index = 0

def merge(a, b):
    global point_on_line
    global line_index
    a_line = point_on_line[a]
    b_line = point_on_line[b]
    if a_line is None and b_line is None:
        point_on_line[a] = line_index
        point_on_line[b] = line_index
        lines.append([a, b])
        line_index += 1
        return line_index - 1
    elif a_line is not None and b_line is not None:
        if a_line != b_line:
            for p in lines[b_line]:
                point_on_line[p] = a_line
            lines[a_line] += lines[b_line]
            lines[b_line] = []
        return a_line
    elif a_line is None:
        point_on_line[a] = b_line
        lines[b_line].append(a)
        return b_line
    elif b_line is None:
        point_on_line[b] = a_line
        lines[a_line].append(b)
        return a_line

for d in distances:
    a,b = d[0],d[1]
    l = merge(a, b)
    if len(lines[l]) == len(points):
        print(d[2][0] * d[3][0])
        break
