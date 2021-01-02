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

#part two
def getVisibleSeats(x,y,seats):
    visibleCells = []
    for offsetRowCol in CORNER_INCLUDED:
        newX = x
        newY = y
        while newY < len(seats) and newY >= 0 and newX < len(seats[0]) and newX >= 0: 
            newY = newY + offsetRowCol[1]
            newX = newX + offsetRowCol[0]
            if newY >= len(seats) or newY < 0 or newX >= len(seats[0]) or newX < 0:
                continue
            cell = seats[newY][newX]
            if cell != ".":
                visibleCells.append(cell)
                #dont look further for seat, the person can only see the first one
                break 
    return visibleCells

def noVisibleOccupiedSeats(x,y,seats):
    visibleSeats = getVisibleSeats(x,y,seats)
    if "#" in visibleSeats:
        return False
    else:
        return True

def fiveOrMoreVisibleSeatsOccupied(x,y,seats):
    visibleSeats = getVisibleSeats(x,y,seats)
    if visibleSeats.count("#") >= 5:
        return True
    else:
        return False

def doRound(seats, type):
    resSeats = deepcopy(seats)
    for y,row in enumerate(seats):
        for x,seat in enumerate(row):
            if seat == ".":
                continue
            if type == "ADJACENT":
                if noAdjacentOccupiedSeats(x,y,seats):
                    resSeats[y][x] = "#"
                elif fourOrMoreAdjacentSeatsOccupied(x,y,seats):
                    resSeats[y][x] = "L"
            elif type == "VISIBLE":
                if noVisibleOccupiedSeats(x,y,seats):
                    resSeats[y][x] = "#"
                elif fiveOrMoreVisibleSeatsOccupied(x,y,seats):
                    resSeats[y][x] = "L"
            else:
                print("error")
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
    currentState = doRound(currentState, "ADJACENT")

print(countOccupiedSeats(currentState))

#part two
previousState = []
currentState = seats
while previousState != currentState:
    previousState = deepcopy(currentState)
    currentState = doRound(currentState, "VISIBLE")

print(countOccupiedSeats(currentState))