

with open("in.txt", "r") as f:
    lines = [op.strip() for op in f.readlines()]
    ops = [(line[0], int(line[1:])) for line in lines]

dial = 50
zero_count = 0
for dir, count in ops:
    if dir == 'R':
        dial += count
    else:
        dial -= count

    dial %= 100
    if dial == 0:
        zero_count += 1

print(zero_count)

