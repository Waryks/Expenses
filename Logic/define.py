from Domain.getters import getId
from Domain.createExpenses import createExpenses
def addExpenses(listOfApartments, expense):
    '''
        Desc: Adds expenses for a specific apartment
        In: listOfApartments - list, expense - list
        Out: -
    '''
    listOfApartments.append(expense)

def modifyExpenses(listOfApartments, apartment, newType, newDate, newSum):
    '''
        Desc: Modifies a specific type of expense for a apartment
        In: listOfApartments - list, apartment - int, type - string, date - string
        Out: -
    '''
    for index in range(len(listOfApartments)):
        if getId(listOfApartments[index]) == apartment:
            ap = createExpenses(apartment,newSum,newDate,newType)
            listOfApartments.pop(index)
            listOfApartments.insert(index,ap)
            break
def removeAp(listOfApartments, apartment):
    for index in range(len(listOfApartments)):
        if getId(listOfApartments[index])==apartment:
            listOfApartments.pop(index)
            break
