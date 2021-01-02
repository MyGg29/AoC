from copy import deepcopy,copy
with open("in") as fIn: 
   seats = fIn.read().split("\n")

seats = [ 
    [seat for seat in row] for row in seats
]

CORNER_INCLUDED = [
    [-1,-1],[-1, 0],[-1, 1],
    [ 0,-1],        [ 0, 1], 
    [ 1,-1],[ 1, 0],[ 1, 1],
]

def isSeatEmpty(x,y, seats):
    return seats[y][x] == "L"


def getAdjacentSeats(x,y,seats):
    adjacentCells = []
    for offsetRowCol in CORNER_INCLUDED:
        newY = y + offsetRowCol[1]
        newX = x + offsetRowCol[0]
        if newY >= len(seats) or newY < 0 or newX >= len(seats[0]) or newX < 0:
            continue
        cell = seats[newY][newX]
        adjacentCells.append(cell)
    return adjacentCells

def noAdjacentOccupiedSeats(x,y,seats):
    adjacentCells = getAdjacentSeats(x,y,seats)
    if "#" in adjacentCells:
        return False
    else:
        return True
def fourOrMoreAdjacentSeatsOccupied(x,y,seats):
    adjacentCells = getAdjacentSeats(x,y,seats)
    if adjacentCells.count("#") >= 4:
        return True
    else:
        return False

def doRound(seats):
    resSeats = deepcopy(seats)
    for y,row in enumerate(seats):
        for x,seat in enumerate(row):
            if seat == ".":
                continue
            if noAdjacentOccupiedSeats(x,y,seats):
                resSeats[y][x] = "#"
            elif fourOrMoreAdjacentSeatsOccupied(x,y,seats):
                resSeats[y][x] = "L"
    return resSeats

def printSeats(seats):
    for row in seats:
        print("".join(row))

def countOccupiedSeats(seats):
    count = 0
    for row in seats:
        count += row.count("#")
    return count


previousState = []
currentState = seats
while previousState != currentState:
    previousState = deepcopy(currentState)
    currentState = doRound(currentState)

print(countOccupiedSeats(currentState))