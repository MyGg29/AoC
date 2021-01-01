with open("in") as fIn: 
   numbers = fIn.read().split("\n")
numbers = list(map(lambda a: int(a), numbers))

res = 0
preambleSize = 25
slidingList = []
for number in numbers:
    if len(slidingList) < preambleSize:
        slidingList.append(int(number))
    else:
        found = False
        for i,leftSide in enumerate(slidingList):
            for j,rightSide in enumerate(slidingList):
                if i == j:
                    continue
                if leftSide + rightSide == number:
                    found = True
                    break
            if found:
                break
        if found:
            slidingList.pop(0)
            slidingList.append(number)
        else:
            res = number
            break
print(res)

#part two
target = res
continuousSum = []
i = 0
while target != sum(continuousSum):
    continuousSum.append(numbers[i])
    while sum(continuousSum)> target:
        continuousSum.pop(0)
    i += 1

res = min(continuousSum) + max(continuousSum)
print(res)