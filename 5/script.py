import math
from functools import reduce
with open("in") as fIn: 
   seats = fIn.read().split("\n")

def getRow(seat):
    min = 0
    max = 127
    for i in range(7):
        direction = seat[i]
        if direction == "F":
            max = max - math.ceil((max-min)/2)
        if direction == "B":
            min = min + math.ceil((max-min)/2)
    return min

def getCol(seat):
    min = 0
    max = 7
    for i in range(7,10):
        direction = seat[i]
        if direction == "L":
            max = max - math.ceil((max-min)/2)
        if direction == "R":
            min = min + math.ceil((max-min)/2)
    return min


def getSeatId(seat):
    row = getRow(seat)
    col = getCol(seat)
    return row * 8 + col

max = 0
for seat in seats:
    seatId = getSeatId(seat)
    if seatId > max:
        max = seatId

print(max)

#part two
plane = []
for seat in seats:
    seatId = getSeatId(seat)
    plane.append(seatId)

plane.sort()
for i in range(len(plane)):
    if i+1 == len(plane):
        #prevent index error when reaching the end of the plane
        continue
    if plane[i]+1 != plane[i+1]:
        print(plane[i] + 1)

