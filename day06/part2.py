from math import prod

with open("in.txt", "r") as f:
    lines = [line[:-1] for line in f.readlines() if line]

ops = lines[-1].split()
nums_t = [line for line in lines[:-1]]
nums = ["".join(row).strip() for row in zip(*nums_t)]

num_groups = []
temp = []
for s in nums:
    if not s:
        if temp:
            num_groups.append(temp)
        temp = []
    else:
        temp.append(s)
if temp:
    num_groups.append(temp)

total = 0

for i, op in enumerate(ops):
    if op == "*":
        total += prod(map(int, num_groups[i]))
    else:
        total += sum(map(int, num_groups[i]))

print(total)
