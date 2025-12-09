with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

num_rows = len(lines)
num_cols = len(lines[0])

border = ["."] * (num_cols + 2)
rows = [border]
rows.extend([[".", *line, "."] for line in lines])
rows.append(border)

deltas = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy]

total = 0
rows_del = []
while True:
    rows_del = [r[:] for r in rows]
    for i in range(1, num_rows + 1):
        for j in range(1, num_cols + 1):
            if rows[i][j] == ".":
                continue
            num_neighbors = 0
            for di, dj in deltas:
                if rows[i + di][j + dj] in {"@", "x"}:
                    num_neighbors += 1

            if num_neighbors < 4:
                rows_del[i][j] = "."
                rows[i][j] = "x"
                total += 1

    if rows == rows_del:
        break

    rows = [["." if s == "x" else s for s in row] for row in rows]

print(total)
