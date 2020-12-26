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

madatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optionalFields = ["cid"]
res = 0
for passport in passports:
    #print(passport)
    labels = [label.split(":")[0] for label in passport]
    valid = True
    for mandatoryField in madatoryFields:
        if mandatoryField not in labels:
            valid = False
    if valid == True:
        res += 1

print(res)