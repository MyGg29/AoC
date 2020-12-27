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