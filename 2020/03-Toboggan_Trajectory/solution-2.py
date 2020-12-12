rows = []

with open("input") as i_file:
    for line in i_file:
        rows.append(line.strip())

xbound = len(rows[0])


x = [0, 0, 0, 0, 0]
x_add = [1, 3, 5, 7, 1]
y = [0, 0, 0, 0, 0]
y_add = [1, 1, 1, 1, 2]
crashes = [0, 0, 0, 0, 0]

for row in rows:
    for i in range(len(x)):
        if y[i] > len(rows):
            continue
        if rows[y[i]][x[i]] == '#':
            crashes[i]+=1
    y = [y[i]+y_add[i] for i in range(len(y))]
    x = [x[i]+x_add[i] for i in range(len(x))]
    for i in range(len(x)):
        if x[i] >= xbound:
            x[i]-=xbound

print(crashes)
print(crashes[0]*crashes[1]*crashes[2]*crashes[3]*crashes[4])