import input

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
points = [list(map(int, line.split(','))) for line in lists]

m_area = 0
n_points = len(points)

for i in range(n_points-1):
    for j in range(i, n_points):
        a = (abs(points[i][0]-points[j][0]) + 1) * (abs(points[i][1]-points[j][1]) + 1)
        m_area = max(m_area, a)
print(m_area)


