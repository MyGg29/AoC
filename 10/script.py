from functools import reduce
with open("in") as fIn: 
   adaptaters = fIn.read().split("\n")
adaptaters = list(map(lambda a: int(a), adaptaters))

#source is 0 jolt
adaptaters.append(0)
#target is max() + 3
adaptaters.append(max(adaptaters) + 3)
adaptaters.sort()

print(adaptaters)
    
jolts = {
    "#1JoltDiff": 0,
    "#3JoltDiff": 0
}
def countJolts(previous,next):
    if next - previous == 1:
        jolts["#1JoltDiff"] += 1
    if next - previous == 3:
        jolts["#3JoltDiff"] += 1
    return next
reduce(countJolts,adaptaters)
res = jolts["#1JoltDiff"] * jolts["#3JoltDiff"]

print(res)