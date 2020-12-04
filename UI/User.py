from UI.menu import menu
from Domain.writeReadFile import writeFile
from Logic.cases import *
import copy


def userInterface(expensesList):
    op = menu()
    commands = []
    commands.append([])
    com_index = 0
    current_index = 0
    while op != 'stop' and op != 'Stop':
        if isInt(op):
            op = int(op)
            if op == 1:
                apart = input("Apartment number: ")
                while isApartment(apart) == False:
                    apart = input("Apartment number and this time a correct one: ")
                apart = int(apart)
                val = input("Expenses cost: ")
                while isPozFloat(val) == False:
                    val = input("Expenses cost and this time a correct one: ")
                val = float(val)
                date = input("Date DD/MM/YY: ")
                while isDate(date) == False:
                    date = input("Better luck next time with your dates: ")
                type = input("Expenses type: ")
                if type in 'maintenance':
                    type = 'maintenance'
                elif type in 'sewer':
                    type = 'sewer'
                elif type in 'others':
                    type = 'others'
                from Domain.createExpenses import createExpenses
                from Logic.define import  addExpenses
                expense = createExpenses(apart, val, date, type)
                addExpenses(expensesList, expense)
                if com_index != current_index:
                    for index in range(current_index+1,com_index+1):
                        commands.pop()
                    com_index = current_index
                commands.append(dipCopy(expensesList))
                current_index += 1
                com_index += 1
            elif op == 2:
                if len(expensesList):
                    apart = input("Apartment number: ")
                    while isApartment(apart) == False:
                        apart = input("Apartment number and this time a correct one: ")
                    apart = int(apart)
                    val = input("New expenses cost: ")
                    while isPozFloat(val) == False:
                        val = input("New expenses cost and this time a correct one: ")
                    val = float(val)
                    date = input("New date DD/MM/YY: ")
                    while isDate(date) == False:
                        date = input("Better luck next time with your dates: ")
                    type = input("Expenses type: ")
                    if type in 'maintenance':
                        type = 'maintenance'
                    elif type in 'sewer':
                        type = 'sewer'
                    elif type in 'others':
                        type = 'others'
                    from Logic.define import modifyExpenses
                    modifyExpenses(expensesList, apart, type, date, val)
                    if com_index != current_index:
                        for index in range(current_index + 1, com_index + 1):
                            commands.pop()
                        com_index = current_index
                    commands.append(dipCopy(expensesList))
                    current_index += 1
                    com_index += 1
                else:
                    print("There are no expenses to be modified!")
            elif op == 3:
                if len(expensesList):
                    apart = input("Apartment number to which an expense is to be deleted: ")
                    while isApartment(apart) == False:
                        apart = input("Apartment number and this time a correct one: ")
                    apart = int(apart)
                    from Logic.define import removeAp
                    removeAp(expensesList, apart)
                    if com_index != current_index:
                        for index in range(current_index + 1, com_index + 1):
                            commands.pop()
                        com_index = current_index
                    commands.append(dipCopy(expensesList))
                    current_index += 1
                    com_index += 1
                else:
                    print("There are no expenses to be deleted!")
            elif op == 4:
                if len(expensesList):
                    apart = input("Apartment number to which all expenses are to be deleted: ")
                    while isApartment(apart) == False:
                        apart = input("Apartment number and this time a correct one: ")
                    apart = int(apart)
                    from Logic.removeExpenses import removeAllExpenses
                    removeAllExpenses(expensesList, apart)
                    if com_index != current_index:
                        for index in range(current_index + 1, com_index + 1):
                            commands.pop()
                        com_index = current_index
                    commands.append(dipCopy(expensesList))
                    current_index += 1
                    com_index += 1
                else:
                    print("There are no expenses to be deleted!")
            elif op == 5:
                if len(expensesList):
                    val = input("The value to be added to the expenses in the certain date: ")
                    while isPozFloat(val) == False:
                        val = input("Expenses cost and this time a correct one: ")
                    val = float(val)
                    date = input("The date in which all expenses are to be changed DD/MM/YY: ")
                    while isDate(date) == False:
                        date = input("Better luck next time with your dates: ")
                    from Logic.addValueToAllExpenses import addValueToAllExpenses
                    addValueToAllExpenses(expensesList, val, date)
                    if com_index != current_index:
                        for index in range(current_index + 1, com_index + 1):
                            commands.pop()
                        com_index = current_index
                    commands.append(dipCopy(expensesList))
                    current_index += 1
                    com_index += 1
                else:
                    print("There are no expenses!")
            elif op == 6:
                if len(expensesList):
                    from Logic.maxExpense import maxExpenses
                    print(maxExpenses(expensesList))
                else:
                    print("There are no expenses!")
            elif op == 7:
                if len(expensesList):
                    from Logic.expensesDescendingOrder import sortExpenses
                    sortExpenses(expensesList)
                    if com_index != current_index:
                        for index in range(current_index + 1, com_index + 1):
                            commands.pop()
                        com_index = current_index
                    commands.append(dipCopy(expensesList))
                    current_index += 1
                    com_index += 1
                else:
                    print("There are no expenses to be ordered!")
            elif op == 8:
                if len(expensesList):
                    from Logic.monthlyExpenses import monthlyExpenses
                    print(monthlyExpenses(expensesList))
                else:
                    print("No expenses to be found!")
            elif op == 9:
                if commands:
                    current_index -= 1
                    while len(expensesList):
                        expensesList.pop()
                    if current_index >= 0:
                        expensesList = dipCopy(commands[current_index])
                    else:
                        expensesList = dipCopy([])
                        current_index = -1

                else:
                    print("Nothing to be undone")

            elif op == 10:
                if current_index > len(commands) - 1:
                    print("Invalid action")
                else:
                    current_index += 1
                    expensesList = dipCopy(commands[current_index])



            elif op == 11:
                from UI.commandLine import run
                run(expensesList)
            elif op == 12:
                for ap in expensesList:
                    from Domain.getters import getId,getDate,getSum,getType
                    print(
                        'Ap: ' + str(getId(ap)) + ' Date: ' + getDate(ap) + ' Expense: ' + str(getSum(ap)) + ' Type: ' + getType(
                            ap))
        else:
            print("Not a valid option!")
        writeFile(expensesList)
        op = menu()
