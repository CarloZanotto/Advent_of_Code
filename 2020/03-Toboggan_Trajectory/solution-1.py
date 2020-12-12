rows = []
crashed_on_a_tree = 0

with open("input") as i_file:
    for line in i_file:
        rows.append(line.strip())

xbound = len(rows[0])

x = 0
y = 0
for row in rows:
    if rows[y][x] == '#':
        crashed_on_a_tree+=1
    y+=1
    x+=3
    if x >= xbound:
        x-=xbound

print(crashed_on_a_tree)