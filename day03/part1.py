with open("in.txt", "r") as f:
    lines = f.readlines()
    batteries = [[int(c) for c in s.strip()] for s in lines]

total = 0
for bat in batteries:
    best = -1
    for i in range(len(bat)):
        for j in range(i + 1, len(bat)):
            v = bat[i] * 10 + bat[j]
            best = max(best, v)

    total += best

print(total)
