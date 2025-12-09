import heapq

with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

points = [tuple(map(int, line.split(","))) for line in lines]
dists = {}

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1, p2 = points[i], points[j]
        d = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
        dists[(p1, p2)] = d

n_closest = heapq.nsmallest(1000, dists.keys(), key=lambda x: dists[x])

best_entry = n_closest[0]
best_p1 = best_entry[0]
best_p2 = best_entry[1]

circ_idx = {best_p1: 0, best_p2: 0}
circuits = [{best_p1, best_p2}]

for p1, p2 in n_closest[1:]:
    i1 = circ_idx.get(p1, -1)
    i2 = circ_idx.get(p2, -1)

    if i1 < 0 and i2 < 0:
        # create new circuit
        circ_idx[p1] = len(circuits)
        circ_idx[p2] = len(circuits)
        circuits.append({p1, p2})

    elif i1 < 0:
        # add p1 to p2 circuit
        circ_idx[p1] = i2
        circuits[i2].add(p1)

    elif i2 < 0:
        # add p2 to p1 circuit
        circ_idx[p2] = i1
        circuits[i1].add(p2)

    elif i1 != i2:
        # merge
        for p in circuits[i2]:
            circ_idx[p] = i1
        circuits[i1].update(circuits[i2])
        circuits[i2].clear()


top3 = heapq.nlargest(3, circuits, key=lambda x: len(x))
prod = 1
for c in top3:
    prod *= len(c)

print(prod)
