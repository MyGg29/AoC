with open("in") as fIn: 
   forest = fIn.read().split("\n")

def parseForest(forest):
    res = []
    for row in forest:
        res.append([square for square in row])

    return res
res = 0
forest = parseForest(forest)
bottom = len(forest) - 1
modulo = len(forest[0])
positionX, positionY = [0,0]
while positionY != bottom:
    positionX = (positionX + 3)%modulo
    positionY = positionY + 1
    if(forest[positionY][positionX] == "#"):
        res += 1

print(res)
