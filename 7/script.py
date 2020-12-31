with open("in") as fIn: 
   bags = fIn.read().split("\n")

def parseBags(bagsStr):
    bags = {}
    for line in bagsStr:
        words = line.split(" ")
        color = words[0] + " " + words[1]
        bags[color] = []
        contains = " ".join(words[4:])
        for contain in contains.split(", "):
            containWords = contain.split(" ")
            containAmount = containWords[0] 
            containColor = containWords[1] + " " + containWords[2]
            bags[color].append({
                "color": containColor,
                "amount": containAmount
            })
    return bags

def checkBag(bag,targetColor, bags):
    if bag == "other bags.":
        return 0
    if bag == targetColor:
        return 1
    else:
        colorsInsideThisBag = [content["color"] for content in bags[bag]]
        ok = []
        #recursion WAYTOODANK
        for color in colorsInsideThisBag:
            ok.append(checkBag(color, targetColor, bags))
        return max(ok)
bags = parseBags(bags)
res = 0
targetBag = "shiny gold"
for k,v in bags.items():
    if k != targetBag:
        res += checkBag(k, targetBag, bags)

print(res)

#part two
def countBag(targetColor, bags, amount):
    amount = []
    for bag in bags[targetColor]:
        if bag["amount"] == "no":
            continue
        amount.append(int(bag["amount"]))
        amount.append(int(bag["amount"]) * countBag(bag["color"], bags, amount))
    return sum(amount)

targetBag = "shiny gold"
res = countBag(targetBag, bags, 0)

print(res)