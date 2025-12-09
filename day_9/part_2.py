
import input

def build_poly(points):
    edges = {}

    for i in range(n_points):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n_points]

        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        # vertical
        if x1 == x2:
            for y in range(y1, y2 + 1):
                if y not in edges:
                    edges[y] = [x1, x1]
                else:
                    edges[y][0] = min(edges[y][0], x1)
                    edges[y][1] = max(edges[y][1], x1)

        # horizontal
        elif y1 == y2:
            if y1 not in edges:
                edges[y1] = [x1, x2]
            else:
                edges[y1][0] = min(edges[y1][0], x1, x2)
                edges[y1][1] = max(edges[y1][1], x1, x2)
    return edges

def is_rect_in_poly(p1, p2, edges):
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    for y in range(min_y, max_y + 1):
        if y not in edges:
            return False
        if min_x < edges[y][0] or max_x > edges[y][1]:
            return False

    return True

# lists = input.sample
lists = input.input
lists = lists.split("\n")[1:-1]
points = [list(map(int, line.split(','))) for line in lists]
n_points = len(points)

edges = build_poly(points)
m_area = 0
for i in range(n_points - 1):
    for j in range(i + 1, n_points):
        if is_rect_in_poly(points[i], points[j], edges):
            a = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
            m_area = max(m_area, a)

print(m_area)
