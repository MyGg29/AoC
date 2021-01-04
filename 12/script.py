with open("in") as fIn: 
   instructions = fIn.read().split("\n")


vectors = {
    "N":0,
    "W":0,
    "S":0,
    "E":0
}
facing = "E"
for instruction in instructions:
    direction = instruction[0]
    value = int(instruction[1:])
    cardinals = list(vectors.keys())
    for possibleDirection in cardinals:
        if direction == possibleDirection:
            vectors[direction] += value
    if direction == "F":
        vectors[facing] += value
    if direction in ["R", "L"]:
        quarters = int(value/90)
        index = cardinals.index(facing)
        if direction == "R":
            facing = cardinals[(index - quarters)%4]
        if direction == "L":
            facing = cardinals[(index + quarters)%4]

position = [
    vectors["N"] - vectors["S"],
    vectors["W"] - vectors["E"],
]
#print(vectors)
#print(position)

manathanLength = abs(position[0]) + abs(position[1])
print(manathanLength)

#part two
#I had a pretty bad data structure in part one for part two

import math

def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

waypoint = {"x": 10, "y": 1}
boat = {"x":0,"y":0}

for instruction in instructions:
    direction = instruction[0]
    value = int(instruction[1:])
    if direction == "N":
        waypoint["y"] += value
    if direction == "S":
        waypoint["y"] -= value
    if direction == "E":
        waypoint["x"] += value
    if direction == "W":
        waypoint["x"] -= value
    if direction == "F":
        boat["x"] = boat["x"] + waypoint["x"]*value
        boat["y"] = boat["y"] + waypoint["y"]*value
    if direction in ["R", "L"]:
        if direction == "R":
            value = -value
        waypoint["x"], waypoint["y"] = rotate((0,0), (waypoint["x"], waypoint["y"]), math.radians(value))

res = abs(boat["x"]) + abs(boat["y"])
print(res)
