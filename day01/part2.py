with open("in.txt", "r") as f:
    lines = [op.strip() for op in f.readlines()]
    ops = [(line[0], int(line[1:])) for line in lines]

# ops = [("L", 50)]

dial = 50
zero_count = 0
for dir, count in ops:
    hits = 0
    
    if dir == "R":
        dial += count
        hits += dial // 100
    else:
        if dial == 0: # don't count start at 0 and go left
            hits -= 1
        dial -= count
        hits += abs(dial // 100)
        if dial % 100 == 0:
            hits += 1

    zero_count += hits
    dial %= 100


print(zero_count)
