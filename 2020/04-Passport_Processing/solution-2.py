import re

passports = []
valid_passports = 0

def birthcheck(data):
    if int(data) in range(1920, 2003):
        return True
    else:
        return False

def issuecheck(data):
    if int(data) in range(2010, 2021):
        return True
    else:
        return False

def expirationcheck(data):
    if int(data) in range(2020, 2031):
        return True
    else:
        return False

def heightcheck(data):
    if re.search("^\d\d\dcm$", data):
        if int(data[:3]) in range(150, 194):
            return True
    elif re.search("^\d\din$", data):
        if int(data[:2]) in range (59, 77):
            return True
    else:
        return False

def haircolorcheck(data):
    if re.search("^#{1}[0-9a-f]{6}$", data):
        return True
    else:
        return False


def eyecolorcheck(data):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if data in eye_colors:
        return True
    else:
        return False

def passportidcheck(data):
    if re.search("^\d{9}$", data):
        return True
    else:
        return False


with open("input") as i_file:
    passport = ["", "", "", "", "", "", "", ""]
    for line in i_file:
        if line in ['\n', '\r\n']:
            passports.append(passport)
            passport = ["", "", "", "", "", "", "", ""]    
        else:
            for field in line.split():
                pre = field[:3]
                data = field[4:]
                if pre == "byr":
                    if birthcheck(data):
                        passport[0] = data
                elif pre == "iyr":
                    if issuecheck(data):
                        passport[1] = data
                elif pre == "eyr":
                    if expirationcheck(data):
                        passport[2] = data
                elif pre == "hgt":
                    if heightcheck(data):
                        passport[3] = data
                elif pre == "hcl":
                    if haircolorcheck(data):
                        passport[4] = data
                elif pre == "ecl":
                    if eyecolorcheck(data):    
                        passport[5] = data
                elif pre == "pid":
                    if passportidcheck(data):
                        passport[6] = data                
                elif pre == "cid":
                    passport[7] = data
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