from Domain.getters import getDate,getType,getId,getSum
from Logic.define import modifyExpenses
from Domain.createExpenses import createExpenses

def addValueToAllExpenses(listOfApartments, value, date):
    '''
        Desc: Adds a value to all the expenses
        In: listOfApartments - list, value - int
        Out: -
     '''
    for index in range(len(listOfApartments)):
        if getDate(listOfApartments[index]) == date:
            ap = createExpenses(getId(listOfApartments[index]),getSum(listOfApartments[index])+value,date,getType(listOfApartments[index]))#str(apartment) + str(newSum) + newDate + newType
            listOfApartments.pop(index)
            listOfApartments.insert(index,ap)
            index -= 1
