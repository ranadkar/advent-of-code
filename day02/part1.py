with open("in.txt", "r") as f:
    input = f.read().strip()
    ranges_str = [tuple(r.strip().split("-")) for r in input.split(",")]

# ranges_str = [("998", "1012")]

total = 0
for low_str, high_str in ranges_str:
    # odd length can never be repeat
    if len(low_str) % 2 == 1 and len(low_str) == len(high_str):
        continue

    length = len(low_str)

    if length % 2 == 0:
        half_len = length // 2
        left_half = int(low_str[:half_len])
        if left_half < int(low_str[half_len:]):
            left_half += 1

        candidate = int(f"{left_half}{left_half}")
        while candidate <= int(high_str):
            total += candidate
            left_half += 1
            candidate = int(f"{left_half}{left_half}")

    for length in range(len(low_str) + 1, len(high_str) + 1):
        if length % 2 == 1:
            continue

        half_len = length // 2

        left_half = 10 ** (half_len - 1)
        candidate = int(f"{left_half}{left_half}")
        while candidate <= int(high_str):
            total += candidate
            left_half += 1
            candidate = int(f"{left_half}{left_half}")

print(total)
