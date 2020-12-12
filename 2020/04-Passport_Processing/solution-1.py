passports = []

valid_passports = 0

with open("input") as i_file:
    passport = ["", "", "", "", "", "", "", ""]
    for line in i_file:
        if line in ['\n', '\r\n']:
            passports.append(passport)
            passport = ["", "", "", "", "", "", "", ""]    
        else:
            for field in line.split():
                if field[:3] == "byr":
                    passport[0] = field[4:]
                elif field[:3]  == "iyr":
                    passport[1] = field[4:]
                elif field[:3]  == "eyr":
                    passport[2] = field[4:]
                elif field[:3]  == "hgt":
                    passport[3] = field[4:]
                elif field[:3]  == "hcl":
                    passport[4] = field[4:]
                elif field[:3]  == "ecl":
                    passport[5] = field[4:]
                elif field[:3]  == "pid":
                    passport[6] = field[4:]                
                elif field[:3]  == "cid":
                    passport[7] = field[4:]
    else:
        passports.append(passport)

for passport in passports:
    counter = 0
    for field in range(7):
        if passport[field] == "":
            counter+=1
    if counter == 0:
        valid_passports+=1

print(valid_passports)
            