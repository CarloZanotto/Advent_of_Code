passwords = []
correct_passwords = 0

with open("input") as i_file:
    for line in i_file:
        passwords.append(line.split())

for line in passwords:
    counter = 0
    for char in line[3]:
        if char == line[2]:
            counter+=1
    if (counter >= int(line[0]) and counter <= int(line[1])):
        correct_passwords+=1

print(correct_passwords)