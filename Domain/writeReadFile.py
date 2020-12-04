import json
FILE_NAME = 'expenses.txt'

def writeFile(expensesList):
    with open(FILE_NAME,'w') as fw:
        json.dump(expensesList, fw)


def readFile():
    with open(FILE_NAME, 'r') as fr:
        expensesList = json.load(fr)
    return expensesList