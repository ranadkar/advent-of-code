with open("in.txt", "r") as f:
    input = f.read().strip()
    ranges_str = [tuple(r.strip().split("-")) for r in input.split(",")]

# ranges_str = [("798", "1212")]

invalids = set()
check_lens = {
    2: {1},
    3: {1},
    4: {2},
    5: {1},
    6: {2, 3},
    7: {1},
    8: {4},
    9: {3},
    10: {2, 5},
    11: {1},
}

for low_str, high_str in ranges_str:

    length = len(low_str)

    for length in range(len(low_str), len(high_str) + 1):
        if length == 1:
            continue
        for sublen in check_lens[length]:
            factor = length // sublen
            pattern = 10 ** (sublen - 1)
            candidate = int(factor * str(pattern))

            while(candidate < int(low_str)):
                pattern += 1
                candidate = int(factor * str(pattern))

            while(candidate <= int(high_str)):
                invalids.add(candidate)
                pattern += 1
                candidate = int(factor * str(pattern))

print(sum(invalids))
