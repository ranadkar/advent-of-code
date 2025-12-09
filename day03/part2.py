with open("in.txt", "r") as f:
    lines = f.readlines()
    batteries = [[int(c) for c in s.strip()] for s in lines]

total = 0
for bat in batteries:
    num_left = 12
    st = []

    for i, d in enumerate(bat):
        while st and d > st[-1] and (len(bat) - i - 1 >= num_left):
            st.pop()
            num_left += 1

        if len(st) < 12:
            st.append(d)
            num_left -= 1

    best = int("".join(map(str, st)))
    total += best

print(total)
