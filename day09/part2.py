with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

points = [tuple(map(int, line.split(","))) for line in lines]
n = len(points)

edges = [(points[i], points[(i + 1) % n]) for i in range(n)]
points_set = set(points)


def in_polygon(p):
    if p in points_set:
        return True

    px, py = p
    inside = False

    for (x1, y1), (x2, y2) in edges:
        if x1 == x2 and px == x1 and min(y1, y2) <= py <= max(y1, y2):
            return True

        if y1 == y2 and py == y1 and min(x1, x2) <= px <= max(x1, x2):
            return True

        if x1 > px and x1 == x2 and min(y1, y2) < py <= max(y1, y2):
            inside = not inside

    return inside


def edge_cross(p1, p2):
    xmin, xmax = min(p1[0], p2[0]), max(p1[0], p2[0])
    ymin, ymax = min(p1[1], p2[1]), max(p1[1], p2[1])

    for (x1, y1), (x2, y2) in edges:
        if x1 == x2:
            if xmin < x1 < xmax and ymin < max(y1, y2) and ymax > min(y1, y2):
                return True
        else:
            if ymin < y1 < ymax and xmin < max(x1, x2) and xmax > min(x1, x2):
                return True

    return False


best = -1
for i in range(n):
    for j in range(i + 1, n):
        p1, p2 = points[i], points[j]
        p3 = (p1[0], p2[1])
        p4 = (p2[0], p1[1])

        if in_polygon(p3) and in_polygon(p4) and not edge_cross(p1, p2):
            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            best = max(best, w * h)

print(best)
