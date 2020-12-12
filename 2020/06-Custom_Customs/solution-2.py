forms = []

with open("input") as i_file:
    form = ""
    lcount = 0
    for line in i_file:
        if line in ['\n', '\r\n']:
            forms.append(["".join(sorted(form)), lcount])
            form = ""
            lcount = 0
        else:
            lcount+=1
            for singlet in line.strip():
                if singlet.isalpha():
                    form += singlet
    else:
        forms.append(["".join(sorted(form)), lcount])

answers = 0

for form in forms:
    for char in forms[0]:
        

print(answers)
            