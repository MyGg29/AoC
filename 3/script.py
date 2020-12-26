with open("in") as fIn: 
   forest = fIn.read().split("\n")

def parseForest(forest):
    res = []
    for row in forest:
        res.append([square for square in row])

    return res
def countEncounteredTrees(slopX, slopY, forest):
    res = 0
    bottom = len(forest) - 1
    modulo = len(forest[0])
    positionX, positionY = [0,0]
    while positionY != bottom:
        positionX = (positionX + slopX)%modulo
        positionY = positionY + slopY
        if(forest[positionY][positionX] == "#"):
            res += 1
    return res
forest = parseForest(forest)
print(countEncounteredTrees(3,1,forest))

#part two
treeEncounteredForSlops = [
    countEncounteredTrees(1,1,forest),
    countEncounteredTrees(3,1,forest),
    countEncounteredTrees(5,1,forest),
    countEncounteredTrees(7,1,forest),
    countEncounteredTrees(1,2,forest)
]
from functools import reduce
res = reduce(lambda x,y: x*y, treeEncounteredForSlops)
print(res)