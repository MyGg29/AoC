with open("in") as fIn: 
   instructions = fIn.read().split("\n")

accumulator = 0
executedLines = set()
i = 0
while i not in executedLines:
    executedLines.add(i)
    instruction = instructions[i]

    instructionWords = instruction.split(" ")
    operation = instructionWords[0]
    sign = instructionWords[1][0]
    value = int(instructionWords[1][1:])
    if operation == "acc":
        if sign == "-":
            accumulator -= value
        else:
            accumulator += value
    if operation == "nop":
        pass
    if operation == "jmp":
        if sign == "-":
            i -= value + 1
        else:
            i += value - 1
    i += 1

print(accumulator)