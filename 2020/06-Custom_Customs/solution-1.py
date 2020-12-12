forms = []

with open("input") as i_file:
    form = ""
    for line in i_file:
        if line in ['\n', '\r\n']:
            forms.append(form)
            form = ""
        else:
            for singlet in line.strip():
                if singlet.isalpha():
                    form += singlet
    else:
        forms.append(form)

answers = 0

for i in range(len(forms)):
    forms[i] = "".join(set(forms[i]))
    answers+=len(forms[i])

print(answers)