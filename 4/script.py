import re
with open("in") as fIn: 
   passportsStr = fIn.read().split("\n")

passports = []
passport = []
for index, line in enumerate(passportsStr):
    if line == "":
        passports.append(passport)
        passport = []
    else:
        passport += line.split(" ")
    if index == len(passportsStr)-1:
        passports.append(passport)
def isPassportValueValid(label, value):
    if label == "byr" and not(1920 <= int(value) <= 2002):
        return False
    if label == "iyr" and not(2010 <= int(value) <= 2020):
        return False
    if label == "eyr" and not(2020 <= int(value) <= 2030):
        return False
    if label == "hgt":
        # not very elegent :/
        if value[-2:] not in ["cm", "in"]:
            return False
        if value[-2:] == "cm" and not(150 <= int(value[:-2]) <= 193):
            return False
        if value[-2:] == "in" and not(59 <= int(value[:-2]) <= 76):
            return False
    if label == "hcl" and not re.search("^#([a-f0-9]{6})$",value):
        return False
    if label == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if label == "pid" and not re.search("^([0-9]{9})$", value):
        return False
    if label == "cid":
        return True
    return True



madatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optionalFields = ["cid"]
res = 0
for passport in passports:
    labels = [label.split(":")[0] for label in passport]
    valid = True
    for mandatoryField in madatoryFields:
        if mandatoryField not in labels:
            valid = False
    for field in passport:
        label, value = field.split(":")
        if(label == "hgt"):
            print(label, value)
        if not isPassportValueValid(label, value):
            valid = False
    if valid == True:
        res += 1
print(res)