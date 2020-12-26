with open("in") as fIn: 
   passwords = fIn.read().split("\n")

res = 0
for passwordRule in passwords:
    rule, letter, password = passwordRule.split(" ")
    #remove the `:` after the letter
    letter = letter[0]
    minIteration, maxIteration = rule.split("-")

    numberOfIteration = [char for char in password].count(letter)
    if int(minIteration) <= int(numberOfIteration) <= int(maxIteration):
        res += 1

print(res)

#part two
res = 0
for passwordRule in passwords:
    rule, letter, password = passwordRule.split(" ")
    #remove the `:` after the letter
    letter = letter[0]
    index1, index2 = rule.split("-")

    passwordArray = [char for char in password]
    if (passwordArray[int(index1) - 1] == letter) != (passwordArray[int(index2) - 1] == letter):
        res += 1
print(res)
