with open("in") as fIn: 
   expenseReport = fIn.read().split("\n")
# cast every items to int so we can work peacefully
expenseReport = [int(i) for i in expenseReport]

res = 0
for expenseLeft in expenseReport:
   for expenseRight in expenseReport:
      expenseSum = expenseLeft + expenseRight
      if expenseSum == 2020:
         res = expenseLeft * expenseRight

print(res)

for expenseLeft in expenseReport:
   for expenseRight in expenseReport:
      for expenseMiddle in expenseReport:
         expenseSum = expenseLeft + expenseMiddle + expenseRight
         if(expenseSum == 2020):
            res = expenseLeft * expenseMiddle * expenseRight

print(res)