with open("in.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines() if line.strip()]

tach_idxs = {lines[0].index("S")}

total = 0

for line in lines[1:]:
    new_idxs = set()
    del_idxs = set()
    for i in tach_idxs:
        if line[i] == "^":
            total += 1
            del_idxs.add(i)
            if i - 1 >= 0:
                new_idxs.add(i - 1)
                line[i - 1] = "|"
            if i + 1 < len(line):
                new_idxs.add(i + 1)
                line[i + 1] = "|"
        else:
            line[i] = "|"

    tach_idxs.update(new_idxs)
    tach_idxs.difference_update(del_idxs)

print(total)
