with open("in.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines() if line.strip()]

num_rows = len(lines)
st = [(1, lines[0].index("S"))]
total = 0

while st:
    row, i = st.pop()
    if row == num_rows:
        total += 1
        print("found", total)
        continue
    line = lines[row]
    if line[i] == "^":
        if i - 1 >= 0:
            st.append((row + 1, i - 1))
        if i + 1 < len(line):
            st.append((row + 1, i + 1))
    else:
        st.append((row + 1, i))


print(total)
