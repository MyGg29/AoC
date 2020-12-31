with open("in") as fIn: 
   instructions = fIn.read().split("\n")

def runMachine(instructions):
    accumulator = 0
    executedLines = set()
    i = 0
    while i not in executedLines:
        if 0 <= i < len(instructions):
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
        else:
            break
    return (accumulator, i)

print(runMachine(instructions)[0])

#part two
for i,instruction in enumerate(instructions):
    copyInstructions = instructions.copy()
    instructionWords = instruction.split(" ")
    operation = instructionWords[0]
    acc, lastLine = [0, 0]
    if operation == "jmp":
        copyInstructions[i] = instruction.replace("jmp", "nop")
    if operation == "nop":
        copyInstructions[i] = instruction.replace("nop", "jmp")
    if operation == "acc":
        continue
    acc, lastLine = runMachine(copyInstructions)
    if lastLine == len(instructions):
        print(acc)
