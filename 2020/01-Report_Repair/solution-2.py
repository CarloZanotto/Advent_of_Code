expenses = []

with open("input") as i_file:
    for line in i_file:
        expenses.append(int(line))

expenses.sort()

for i in range(0, len(expenses)-2):
    for j in range(i+1, len(expenses)-1):
        for k in range(j+1, len(expenses)):
            if (expenses[i] + expenses[j] + expenses[k]) >= 2021:
                continue
            elif (expenses[i] + expenses[j] + expenses[k]) == 2020:
                print(expenses[i])
                print(expenses[j])
                print(expenses[k])
                print(expenses[i]+expenses[j]+expenses[k])
                print(expenses[i]*expenses[j]*expenses[k])