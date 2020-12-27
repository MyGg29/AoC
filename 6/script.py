with open("in") as fIn: 
   people = fIn.read().split("\n")

groups = []
group = []
for index,person in enumerate(people):
    if person == "":
        groups.append(group)
        group = []
    else:
        group.append(person)
    if index == len(people)-1:
        groups.append(group)

res = 0
for group in groups:
    questions = ""
    for person in group:
        questions += person
    questionsList = [question for question in questions]
    questionsNoDuplicate = list(dict.fromkeys(questionsList))
    numberOfYes = len(questionsNoDuplicate)
    res += numberOfYes

print(res)

#part two
def handleGroup(group):
    res = 0
    questions = dict.fromkeys([char for char in "abcdefghijklmnopqrstuvwxyz"], 0)
    for person in group:
        for question in person:
            questions[question] += 1
    for question, occurence  in questions.items():
        #print(question, occurence, len(group))
        if occurence == len(group):
            res += 1
    return res

res = 0
for group in groups:
    res += handleGroup(group)

print(res)