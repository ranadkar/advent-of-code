with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

points = [tuple(map(int, line.split(","))) for line in lines]

best = -1
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1, p2 = points[i], points[j]
        w = abs(p1[0] - p2[0]) + 1
        h = abs(p1[1] - p2[1]) + 1
        best = max(best, w * h)

print(best)

