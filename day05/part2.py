with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

ranges = []
vals = []

for line in lines:
    if "-" in line:
        ranges.append(tuple(map(int, line.split("-"))))
    else:
        vals.append(int(line))


ranges.sort()

i = 0
while i < len(ranges) - 1:
    cur, nxt = ranges[i], ranges[i + 1]
    if nxt[0] <= cur[1]:
        ranges[i] = (cur[0], max(cur[1], nxt[1]))
        del ranges[i + 1]
    else:
        i += 1

total = 0
for low, high in ranges:
    total += high - low + 1

print(total)

