with open("in.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines() if line.strip()]

start_i = lines[0].index("S")

counts = [0] * len(lines[0])
counts[start_i] = 1

for line in lines[1:]:
    new_counts = [0] * len(lines[0])
    for i, count in enumerate(counts):
        if line[i] == "^":
            if i - 1 >= 0:
                new_counts[i - 1] += counts[i]

            if i + 1 < len(line):
                new_counts[i + 1] += counts[i]
        else:
            new_counts[i] += counts[i]

    counts = new_counts

print(sum(new_counts))
