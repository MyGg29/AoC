from functools import reduce
with open("in") as fIn: 
   adaptaters = fIn.read().split("\n")
adaptaters = list(map(lambda a: int(a), adaptaters))

#source is 0 jolt
adaptaters.append(0)
#target is max() + 3
adaptaters.append(max(adaptaters) + 3)
adaptaters.sort()

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

#part two
#dynamic programming
dp = [1]
for i in range(1,len(adaptaters)):
    ans = 0
    for j in range(i):
        if adaptaters[j] + 3 >= adaptaters[i]:
            ans += dp[j]
    dp.append(ans)

print(dp[-1])

