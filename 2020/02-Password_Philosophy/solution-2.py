passwords = []
correct_passwords = 0

with open("input") as i_file:
    for line in i_file:
        txt = line.split()
        passwords.append([[int(txt[0])-1, int(txt[1])-1], txt[2], txt[3]])

for line in passwords:
    counter = 0
    for index in line[0]:
        if line[1] == line[2][index]:
            counter+=1
    if counter == 1:
        correct_passwords+=1

print(correct_passwords)