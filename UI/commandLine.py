from Logic import *
from Logic.define import *
from Domain.createExpenses import createExpenses
def instructions():
    print(" add <apartment number> <sum that has to be paid> <date> <type (ex: sewer, maintenance, others)>\n",
          "del <apartment number> <date> <type (ex: sewer, maintenance, others) of the expense that you want to delete>\n",
          "modify <apartment number> <date> <type (ex: sewer, maintenance, others) of the expense that you want to modify> <new sum>\n"
          " delAll <apartment number> to remove all expenses for a apartment\n"
          " addValue <value> <date DD/MM/YY> to add a value to all expenses\n"
          " maxExpense to show the highest expense for each type that there is\n"
          " sortExpense to sort in descending orther the expenses\n"
          "\n info for this information again       exit to quit the program        show to show the expenses and the apartments")
def run(expenses):
    '''
    Add expense
    Del expense
    Modify expense
    '''
    instructions()
    while True:
        command = input()
        command = command.split(";")
        for func in command:
            command_now = func.split(" ")
            if command_now[0] == "info":
                instructions()
            if command_now[0] == "exit":
                return 0
            if command_now[0] == "add":
                c = (str(command_now[1]),str(command_now[2]),str(command_now[3]),str(command_now[4]))
                joinMyString = " ".join(c)
                print (joinMyString)
                #addExpenses(expenses,joinMyString)
                addExpenses(expenses,[int(command_now[1]),float(command_now[2]),str(command_now[3]),str(command_now[4])])
            if command_now[0] == "del":
                from Logic.removeExpenses import removeAllExpenses
                removeAllExpenses(expenses,int(command_now[1]))
            if command_now[0] == "modify":
                modifyExpenses(expenses,int(command_now[1]),str(command_now[3]),str(command_now[2]),float(command_now[4]))
            if command_now[0] == "delAll":
                from Logic.removeExpenses import removeAllExpenses
                removeAllExpenses(expenses,int(command_now[1]))
            if command_now[0] == "addValue":
                from Logic.addValueToAllExpenses import addValueToAllExpenses
                addValueToAllExpenses(expenses,float(command_now[1]),command_now[2])
            if command_now[0] == "maxExpense":
                from Logic.maxExpense import maxExpenses
                print(maxExpenses(expenses))
            if command_now[0] == "sortExpense":
                from Logic.expensesDescendingOrder import sortExpenses
                sortExpenses(expenses)
            if command_now[0] == "show":
                for el in expenses:
                    print(el)