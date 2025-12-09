from math import prod

with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

nums_t = [list(map(int, line.split())) for line in lines[:-1]]
ops = lines[-1].split()

nums = [list(row) for row in zip(*nums_t)]

total = 0

for i, op in enumerate(ops):
    if op == "*":
        total += prod(nums[i])
    else:
        total += sum(nums[i])

print(total)
