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